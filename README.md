# [M1] Fase de Compilación: Análisis Semántico

## 🧰 Instrucciones de Configuración

1. **Construir y Ejecutar el Contenedor Docker:** Desde el directorio raíz, ejecuta el siguiente comando para construir la imagen y lanzar un contenedor interactivo:

```bash
docker build --rm . -t csp-image && docker run --rm -ti -v "$(pwd)/program":/program csp-image

cmd /c "docker build --rm -t csp-image . && docker run --rm -it -v %cd%\program:/program csp-image"

```