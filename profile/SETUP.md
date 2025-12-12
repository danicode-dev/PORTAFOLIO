# Configuración del Perfil

Este repositorio contiene la configuración automática de tu perfil de GitHub.

## Cómo añadir un nuevo proyecto

1.  Edita el archivo `projects/projects.yml`.
2.  Añade una nueva entrada siguiendo este formato:

    ```yaml
    - name: Nombre del Proyecto
      repo: https://github.com/danicode-dev/MI-PROYECTO
      demo: https://danicode-dev.github.io/MI-PROYECTO/
      tech: [Java, HTML]
      status: active  # opciones: featured, active, completed, planned, archived
      desc: "Descripción corta."
    ```

3.  Haz un commit y push:
    ```bash
    git add projects/projects.yml
    git commit -m "Añadir nuevo proyecto"
    git push
    ```

4.  ¡Listo! La GitHub Action se encargará de regenerar el `README.md` principal y el `projects/README.md`.

## Edición Manual

Si quieres cambiar los enlaces de LinkedIn o Email, edita directamente el archivo `README.md` en la raíz.

## Ejecución Local (Opcional)

Si quieres ver los cambios antes de subir:

1.  Instala Python y la librería `pyyaml`:
    ```bash
    pip install pyyaml
    ```
2.  Ejecuta el script:
    ```bash
    python scripts/render_projects.py
    ```
