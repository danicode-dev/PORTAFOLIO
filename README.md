# Portfolio - danicode-dev

Mi portfolio personal hecho con HTML, CSS y JavaScript vanilla.

## 🔗 Demo

https://danicode-dev.github.io/PORTAFOLIO/

## 📂 Estructura

```
index.html      → Página principal
css/styles.css  → Estilos
js/script.js    → Lógica y animaciones
deploy.js       → Script de deploy con cache busting
```

## 🚀 Deploy

Para desplegar cambios con cache busting automático:

```bash
npm run deploy
```

Esto:
1. Calcula hash MD5 de CSS y JS
2. Actualiza `index.html` con los nuevos hashes
3. Hace commit y push a GitHub

## 💻 Local

```bash
# Opción 1: Abrir directamente
start index.html

# Opción 2: Servidor local
python -m http.server 8000
# Ve a http://localhost:8000
```

## 🔄 Forzar recarga

Si el navegador muestra versiones antiguas:

1. **Chrome/Edge**: `Ctrl + Shift + R` (Windows) o `Cmd + Shift + R` (Mac)
2. **Firefox**: `Ctrl + F5`
3. **DevTools**: Pestaña Network → clic derecho → "Clear browser cache"

## ⚠️ Nota sobre GitHub Pages

GitHub Pages cachea archivos ~10 minutos. Tras un deploy:
- Espera 1-2 minutos para que se procese
- Usa recarga forzada (`Ctrl+Shift+R`) si no ves cambios
- El script `deploy.js` añade hashes únicos para evitar caché
