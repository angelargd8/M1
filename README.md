# ANTLR GRAMMAR

### Librerias necesarias:

```
pip install antlr4-tools
-m pip install antlr4-python3-runtime==4.7.2
```

En el caso que no funcionen las librerias por tener python en appdata, instalar antlr en java: 
(nota: esta es la version compatible con java 8)
```
curl -o antlr-4.7.2-complete.jar https://www.antlr.org/download/antlr-4.7.2-complete.jar
```
probar que se instalo:
```
java -jar antlr-4.7.2-complete.jar
```



### generar el lexer y parser:

(nota: se genero el lexer y parser en el de java, por lo tanto es importante estar en la ruta en la que se tiene la gramatica para correr el siguiente comando)
```
java -jar C:\WINDOWS\system32\antlr-4.7.2-complete.jar -Dlanguage=Python3 -visitor SimpleLang.g4            *** Esto es para utilizar un Visitor ***

java -jar C:\WINDOWS\system32\antlr-4.7.2-complete.jar -Dlanguage=Python3 -listener  SimpleLang.g4            *** Esto es para utilizar un Visitor ***

```

la otra forma: 
```
-m antlr4_tools -Dlanguage=Python3 -visitor SimpleLang.g4
-m antlr4_tools -Dlanguage=Python3 -visitor listener.g4
```

Y por ultimo:
```
python3 Driver.py program_test_pass.txt
python3 DriverListener.py program_test_pass.txt
```

o en el caso que en python este en appdata, dejo el ejemplo:
```
& C:/Users/angel/AppData/Local/Programs/Python/Python312/python.exe c:/Users/angel/OneDrive/Documentos/.universidad/.2025/s2/compis/ms/M1/lab2/program/Driver.py program_test_pass.txt

& C:/Users/angel/AppData/Local/Programs/Python/Python312/python.exe c:/Users/angel/OneDrive/Documentos/.universidad/.2025/s2/compis/ms/M1/lab2/program/DriverListener.py program_test_pass.txt


& C:/Users/angel/AppData/Local/Programs/Python/Python312/python.exe c:/Users/angel/OneDrive/Documentos/.universidad/.2025/s2/compis/ms/M1/lab2/program/Driver.py program_test_no_pass.txt

& C:/Users/angel/AppData/Local/Programs/Python/Python312/python.exe c:/Users/angel/OneDrive/Documentos/.universidad/.2025/s2/compis/ms/M1/lab2/program/DriverListener.py program_test_no_pass.txt

```

Casos agregados:
Var, Assign, UnarySign y Pow

Los nombres de los metodos:
Var -> exitVar / visitVar
Assign -> exitAssign / visitAssign
UnarySign -> exitUnarySign / visitUnarySign
Pow -> exitPow / visitPow


Referencias: 
- https://github.com/gbrolo/compilers-2025/
- https://github.com/antlr/antlr4/blob/master/doc/python-target.md
- https://www.antlr.org/download.html
