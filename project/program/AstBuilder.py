from gen.CompiscriptVisitor import CompiscriptVisitor
from gen.CompiscriptParser import CompiscriptParser
from AstNodes import *

#mapear tipos textuales a internos

def map_type(txt: str) -> str:
    t = txt.strip().lower()
    type_map = {
        "int": "int",
        "integer": "int",
        "string": "str",
        "bool": "bool",
        "boolean": "bool",
        "void": "void",
        "float": "float",
        "double": "float"
    }
    return type_map.get(t, t)  # si no esta en el mapa, devolver tal cual (posible clase o struct)

class AstBuilder(CompiscriptVisitor ):
    pass
