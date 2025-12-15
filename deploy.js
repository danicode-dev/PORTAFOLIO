const fs = require('fs');
const crypto = require('crypto');
const { execSync } = require('child_process');
const path = require('path');

// Archivos a versionar
const FILES_TO_HASH = [
    { file: 'css/styles.css', pattern: /\.\/css\/styles\.css\?v=[^"']+/g, template: (h) => `./css/styles.css?v=${h}` },
    { file: 'js/script.js', pattern: /\.\/js\/script\.js\?v=[^"']+/g, template: (h) => `./js/script.js?v=${h}` }
];

const INDEX_FILE = 'index.html';

/**
 * Calcula hash MD5 corto (8 caracteres) de un archivo
 */
function getFileHash(filePath) {
    const fullPath = path.join(__dirname, filePath);
    if (!fs.existsSync(fullPath)) {
        console.error(`❌ Archivo no encontrado: ${filePath}`);
        process.exit(1);
    }
    const content = fs.readFileSync(fullPath);
    return crypto.createHash('md5').update(content).digest('hex').substring(0, 8);
}

/**
 * Actualiza index.html con los nuevos hashes
 */
function updateIndexHtml() {
    const indexPath = path.join(__dirname, INDEX_FILE);
    let html = fs.readFileSync(indexPath, 'utf8');

    const updates = [];

    for (const { file, pattern, template } of FILES_TO_HASH) {
        const hash = getFileHash(file);
        const newRef = template(hash);

        if (pattern.test(html)) {
            html = html.replace(pattern, newRef);
            updates.push(`  ✓ ${file} -> ?v=${hash}`);
        } else {
            console.warn(`⚠️ No se encontró referencia a ${file} en index.html`);
        }
    }

    fs.writeFileSync(indexPath, html, 'utf8');
    return updates;
}

/**
 * Ejecuta comandos git
 */
function gitCommitAndPush(message) {
    try {
        execSync('git add .', { stdio: 'inherit' });
        execSync(`git commit -m "${message}"`, { stdio: 'inherit' });
        execSync('git push origin main', { stdio: 'inherit' });
        return true;
    } catch (error) {
        console.error('❌ Error en git:', error.message);
        return false;
    }
}

// Main
console.log('\n🚀 Deploy con Cache Busting\n');
console.log('📦 Calculando hashes...');

const updates = updateIndexHtml();

if (updates.length === 0) {
    console.log('⚠️ No se actualizaron hashes');
    process.exit(0);
}

console.log('\n📝 Archivos actualizados:');
updates.forEach(u => console.log(u));

const timestamp = new Date().toISOString().replace(/[:.]/g, '-').substring(0, 19);
const commitMessage = `deploy: cache bust ${timestamp}`;

console.log(`\n📤 Commit: "${commitMessage}"\n`);

if (gitCommitAndPush(commitMessage)) {
    console.log('\n✅ Deploy completado!');
    console.log('🌐 Los cambios estarán disponibles en ~1-2 minutos en GitHub Pages\n');
} else {
    console.log('\n❌ Deploy fallido\n');
    process.exit(1);
}
