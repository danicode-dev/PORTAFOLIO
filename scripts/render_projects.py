import yaml
import os

def load_projects():
    with open('projects/projects.yml', 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def generate_tech_badges(tech_list):
    # Mapping tech to skillicons or shields.io style
    # For now, simple text badges or we could use skillicons url builder
    # Using simple text for compactness in the card description, or Shields.io
    badges = []
    for t in tech_list:
        badges.append(f"`{t}`")
    return " ".join(badges)

def generate_featured_markdown(projects):
    featured = [p for p in projects if p.get('status') == 'featured']
    # Limit to 6
    featured = featured[:6]
    
    md = "### \u2B50 Proyectos Destacados (Featured)\n\n"
    # Create a grid or list. Rows of 2 is nice.
    # Markdown table is easiest for grid alignment on GitHub.
    
    md += "| Proyecto | Detalles |\n"
    md += "| :--- | :--- |\n"
    
    for p in featured:
        name = p['name']
        desc = p['desc']
        demo = p['demo']
        repo = p['repo']
        tech = generate_tech_badges(p['tech'])
        
        links = f"[<img src='https://img.shields.io/badge/GitHub-Repo-blue?style=flat-square&logo=github' height='20'>]({repo})"
        if demo and demo != "#":
            links += f" [<img src='https://img.shields.io/badge/Web-Demo-2ea44f?style=flat-square&logo=google-chrome' height='20'>]({demo})"
            
        md += f"| **{name}**<br>{desc} | {tech}<br>{links} |\n"
        
    return md

def generate_catalog_markdown(projects):
    md = "# \uD83D\uDCC1 Catálogo Completo de Proyectos\n\n"
    md += "Lista completa de mis desarrollos, experimentos y prácticas.\n\n"
    
    # Group by status
    status_map = {
        'active': '\uD83D\uDFE2 Activos / En Producción',
        'featured': '\u2B50 Destacados',
        'completed': '\u2705 Completados',
        'planned': '\uD83D\uDEA7 Ideas / En Construcción',
        'archived': '\uD83D\uDCC2 Archivados'
    }
    
    # Sort projects: featured first, then active...
    # Actually just grouping them.
    
    grouped = {}
    for p in projects:
        s = p.get('status', 'other')
        if s not in grouped:
            grouped[s] = []
        grouped[s].append(p)
        
    order = ['featured', 'active', 'completed', 'planned', 'archived']
    
    for s in order:
        if s in grouped:
            md += f"## {status_map.get(s, s.title())}\n\n"
            for p in grouped[s]:
                name = p['name']
                desc = p['desc']
                links = f"[Repo]({p['repo']})"
                if p.get('demo') and p['demo'] != '#':
                    links += f" · [Demo]({p['demo']})"
                
                tech = ", ".join(p['tech'])
                md += f"- **{name}**: {desc}\n  - *Tech*: {tech}\n  - *Links*: {links}\n\n"
                
    return md

def update_readme(featured_content):
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    start_marker = "<!-- PROJECTS:START -->"
    end_marker = "<!-- PROJECTS:END -->"
    
    if start_marker not in content or end_marker not in content:
        print("Markers not found in README.md")
        return
        
    pre = content.split(start_marker)[0]
    post = content.split(end_marker)[1]
    
    new_content = f"{pre}{start_marker}\n{featured_content}\n{end_marker}{post}"
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(new_content)

def main():
    projects = load_projects()
    
    # Generate Featured Block
    featured_md = generate_featured_markdown(projects)
    
    # Update Main README
    # Only update if README exists (it should)
    if os.path.exists('README.md'):
        update_readme(featured_md)
        print("Updated README.md")
    else:
        print("README.md not found, skipping update.")
    
    # Generate Catalog
    catalog_md = generate_catalog_markdown(projects)
    with open('projects/README.md', 'w', encoding='utf-8') as f:
        f.write(catalog_md)
    print("Generated projects/README.md")

if __name__ == "__main__":
    main()
