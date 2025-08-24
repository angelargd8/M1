import sys
from antlr4 import *
from gen.CompiscriptLexer import CompiscriptLexer
from gen.CompiscriptParser import CompiscriptParser

def parse(argv):
    input_stream = FileStream(argv[1], encoding='utf-8')
    lexer = CompiscriptLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CompiscriptParser(stream)
    tree = parser.program()

    errs = parser.getNumberOfSyntaxErrors()
    if errs > 0:
        print(f"Se encontraron {errs} errores de sintaxis.")
        sys.exit(1)

    return tree


def main(argv):
    
    tree = parse(argv)

    # AST - Abstract Syntax Tree 
    
    # tabla de simbolos - con ast o directamente sobre el parse tree recolectar declaraciones y crear ambitos, detectar redeclaraciones y forwars declarations

    # sistema de tipos 

    # manejo de ambito

    # funciones y procedimientos

    #control de flujo

    #clases y objetos

    #listas y estructuras de datos

    # generales - deteccion de codigo muerto, verificacion del sentido semantico, declaraciones duplicadas

    # recorrer el arbol usando listeners o visitors para evaluar las reglas semanticas que se ajusten al lenguaje

    # tests para validar casos exitosos y fallidos

    # tabla de simbolos 

    

if __name__ == '__main__':
    main(sys.argv)