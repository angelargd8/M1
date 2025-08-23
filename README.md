# [M1] Fase de Compilación: Análisis Semántico

## 🧰 Instrucciones de Configuración

1. **Construir y Ejecutar el Contenedor Docker:** Desde el directorio raíz, ejecuta el siguiente comando para construir la imagen y lanzar un contenedor interactivo:

```bash
docker build --rm . -t csp-image && docker run --rm -ti -v "$(pwd)/program":/program csp-image
```

volverlo a correr
```bash
cd ~/compis/M1/project
docker run --rm -it -v "$(pwd)":/program -w /program csp-image
```

activar en venv en wls:
```
python3 -m venv .venv
. .venv/bin/activate
```

instalar antlr:
```
python -m pip install --upgrade pip
pip install "antlr4-python3-runtime==4.13.1"

#comprobar que se instalo:
which python
python -c "import antlr4; print('ANTLR runtime OK')"
```

```
docker run --rm -u "$UIDGID" -v "$(pwd)":/work -w /work csp-image bash -lc 'java -jar /usr/local/lib/antlr-4.13.1-complete.jar -Dlanguage=Python3 -visitor -no-listener -o program/gen program/Compiscript.g4'
```

