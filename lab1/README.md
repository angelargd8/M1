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
java -jar C:\WINDOWS\system32\antlr-4.7.2-complete.jar -Dlanguage=Python3 -visitor Gramatica.g4

```

la otra forma: 
```
-m antlr4_tools -Dlanguage=Python3 -visitor Gramatica.g4

```

Referencias: 
- https://github.com/antlr/antlr4/blob/master/doc/python-target.md
- https://www.antlr.org/download.html
