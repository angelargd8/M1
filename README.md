# [M1] Fase de Compilación: Análisis Semántico

## 🧰 Instrucciones de Configuración

1. **Construir y Ejecutar el Contenedor Docker:** Desde el directorio raíz, ejecuta el siguiente comando para construir la imagen y lanzar un contenedor interactivo:

```bash
docker build --rm . -t csp-image
docker run -ti -v "$(pwd)/program":/program -p 8501:8501 csp-image
```

volverlo a correr
```bash
cd ~/compis/M1/project
docker run --rm -it -v "$(pwd)":/program -w /program csp-image
```

Abrir un nuevo cmd
Usar usuario root de docker
```
docker exec -it --user root <container id> bash
apt update
apt install python3.12-venv
```

Regresar al shell de appuser
activar en venv en el container:
```
python3 -m venv .venv
. .venv/bin/activate
```
Version de python:
```
Python 3.12.3
```

instalar antlr:
```
python -m pip install --upgrade pip
pip install -r requirements.txt 

#comprobar que se instalo:
which python
python -c "import antlr4; print('ANTLR runtime OK')"
```

Correr el IDE
Cambiar al shell root user 
```
streamlit run IDE/app.py
```



```
docker run --rm -u "$UIDGID" -v "$(pwd)":/work -w /work csp-image bash -lc 'java -jar /usr/local/lib/antlr-4.13.1-complete.jar -Dlanguage=Python3 -visitor -no-listener -o program/gen program/Compiscript.g4'
```



Como correr el programa:
python Driver.py program.cps




## 📋 Requerimientos

🟢✅ 1. **Crear un analizador sintáctico utilizando ANTLR** o cualquier otra herramienta similar de su elección
   * Se recomienda usar ANTLR dado que es la herramienta que se utiliza en las lecciones del curso, pero puede utilizar otro Generador de Parsers.

**Analizador léxico:** CompiscriptLexer -> convierte texto -> tokens

**Analizador sintactico:** CompiscriptParser -> tokens -> arbol de parseo

**Analizador sintactico:** tree = parser.program(). A partir de los tokens que produce el lexer y de una gramatica, verifica que la secuencia cumpla con la sintaxis del lenguaje y construye una estructura jerarquja, que en este caso es el arbol de parseo.

-------

2. Añadir **acciones/reglas semánticas** en este analizador sintáctico y **construir un  ́****arbol sintáctico, con una representación visual****.**
   1. **Sistema de Tipos**
      * 🟢 Verificación de tipos en operaciones aritméticas (`+`, `-`, `*`, `/`) — los operandos deben ser de tipo `integer` o `float`.
      *  Verificación de tipos en operaciones lógicas (`&&`, `||`, `!`) — los operandos deben ser de tipo `boolean`.
      * 🟢 Compatibilidad de tipos en comparaciones (`==`, `!=`, `<`, `<=`, `>`, `>=`) — los operandos deben ser del mismo tipo compatible.
      * 🟢 Verificación de tipos en asignaciones — el tipo del valor debe coincidir con el tipo declarado de la variable.
      *  Inicialización obligatoria de constantes (`const`) en su declaración.
      * 🟢 Verificación de tipos en listas y estructuras (si se soportan más adelante).
   2. **Manejo de Ámbito**
      * 🟢 Resolución adecuada de nombres de variables y funciones según el ámbito local o global.
      * 🟢 Error por uso de variables no declaradas.
      * 🟢 Prohibir redeclaración de identificadores en el mismo ámbito.
      * 🟢 Control de acceso correcto a variables en bloques anidados.
      * 🟢 Creación de nuevos entornos de símbolo para cada función, clase y bloque.
   3. **Funciones y Procedimientos**
      * 🟢 Validación del número y tipo de argumentos en llamadas a funciones (coincidencia posicional).
      * 🟢 Validación del tipo de retorno de la función — el valor devuelto debe coincidir con el tipo declarado.
      * 🟢 Soporte para funciones recursivas — verificación de que pueden llamarse a sí mismas.
      * 🟢 Soporte para funciones anidadas y closures — debe capturar variables del entorno donde se definen.
      * 🟢 Detección de múltiples declaraciones de funciones con el mismo nombre (si no se soporta sobrecarga).
      
   4. **Control de Flujo**
      * 🟢 Las condiciones en `if`, `while`, `do-while`, `for`, `switch` deben evaluar expresiones de tipo `boolean`.
      * 🟢 Validación de que se puede usar `break` y `continue` sólo dentro de bucles.
      * 🟢 Validación de que el `return` esté dentro de una función (no fuera del cuerpo de una función).
   5. **Clases y Objetos**
      * 🟢 Validación de existencia de atributos y métodos accedidos mediante `.` (dot notation).
      * 🟢 Verificación de que el constructor (si existe) se llama correctamente.
      * 🟢 Manejo de `this` para referenciar el objeto actual (verificar ámbito).
   6. **Listas y Estructuras de Datos**
      * 🟢 Verificación del tipo de elementos en listas.
      * 🟢 Validación de índices (acceso válido a listas).
   7. **Generales**
      * 🟢 Detección de código muerto (instrucciones después de un `return`, `break`, etc.).
      * 🟢 Verificación de que las expresiones tienen sentido semántico (por ejemplo, no multiplicar funciones).
      * 🟢 Validación de declaraciones duplicadas (variables, parámetros).
3. Implementar la recorrida de este árbol utilizando ANTLR Listeners o Visitors para evaluar las reglas semánticas que se ajusten al lenguaje.
4. **Para los puntos anteriores, referentes a las reglas semánticas, deberá de escribir una batería de tests para validar casos exitosos y casos fallidos en cada una de las reglas mencionadas.**
   * Al momento de presentar su trabajo, esta batería de tests debe estar presente y será tomada en cuenta para validar el funcionamiento de su compilador.
5. Construir una **tabla de símbolos** que interactue con cada fase de la compilación, incluyendo las fases mencionadas anteriormente. Esta tabla debe considerar el **manejo de entornos** y almacenar toda la información necesaria para esta y futuras fases de compilación.
6. Deberá **desarrollar un IDE** que permita a los usuarios escribir su propio código y compilarlo.
7. Deberá crear **documentación asociada a la arquitectura de su implementación** y **documentación de las generalidades de cómo ejecutar su compilador**.
