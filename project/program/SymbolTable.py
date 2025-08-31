from dataclasses import dataclass, field
from typing import Dict, Optional, Any, List

# tabla de simbolo por alcance
# estructura de datos que guarda informacion de los nombres de las variables que hay en un lenguaje de programacion

#representa un tipo, para listas una name="list" s
@dataclass
class TypeSymbol:
    name: str

# representa una variable en la tabla de simbolos
@dataclass
class VariableSymbol:
    name: str
    type: TypeSymbol
    const: bool = False
    initialized: bool = False
    decl_node: Any = None
    line: int = -1
    col: int = -1

# representa una funcion en la tabla de simbolos
@dataclass
class FunctionSymbol:
    #  no defaults
    name: str
    return_type: TypeSymbol
    # defaults 
    params: List[VariableSymbol] = field(default_factory=list)
    is_defined: bool = False
    decl_node: Any = None
    line: int = -1
    col: int = -1

# representa un alcance en la tabla de simbolos
# crea un scope con padre opcional
class Scope: 
    def __init__(self, name: str, parent: Optional['Scope'] = None):
        self.name = name
        self.parent = parent
        self.symbols: Dict[str, Any] = {}  # puede contener VariableSymbol o FunctionSymbol

    #define un simbolo nuevo en el scope actual
    def define(self, sym):
        if sym.name in self.symbols:
            raise Exception(f"Error: '{sym.name}' ya está definido en este alcance.")
        self.symbols[sym.name] = sym

    # busca un simbolo por cadena de scopez hasta la raiz
    def resolve(self, name: str) -> Optional[Any]:
        if name in self.symbols:
            return self.symbols[name]
        if self.parent:
            return self.parent.resolve(name)
        return None
    
# representa la tabla de simbolos completa   
# # inicializa el scope global y registra los tipos base 
#administra scopes y tipos, expone utilidades para definir y resolver simbolos
class SymbolTable:
    def __init__(self):
        self.global_scope = Scope("global")
        self.current_scope = self.global_scope

        self.types: Dict[str, TypeSymbol] = {
            "int": TypeSymbol("int"),
            "float": TypeSymbol("float"),
            "string": TypeSymbol("string"),
            "bool": TypeSymbol("bool"),
            "void": TypeSymbol("void"),
            "list": TypeSymbol("list"), 
        }

    # crea un nuevo scope, entra un nuevo scope hijo y lo devuelve
    def push_scope(self, name: str):
        self.current_scope = Scope(name, self.current_scope)
        return self.current_scope
    
    #sale al scope padre, error si ya esta en el global 
    def pop_scope(self):
        if self.current_scope.parent is None:
            raise Exception("Error: No se puede salir del alcance global.")
        self.current_scope = self.current_scope.parent

    # resuelve un tipo
    def get_type(self, name: str) -> TypeSymbol:
        t = self.types.get(name)
        if t:
            return t
        # soporte arreglos: int[], int[][]
        if name.endswith("]"):
            # normaliza todo lo que termine en [] como 'list'
            return self.types["list"]
        raise Exception(f"Error: Tipo '{name}' no definido.")

    # pop scope en otras palabras jaja
    def exit_scope(self):
        if self.current_scope.parent is not None:
            self.current_scope = self.current_scope.parent
        else:
            raise Exception("Error: No se puede salir del alcance global.")

    #define una variable en el scope actual
    def define_variable(self, var: VariableSymbol):
        self.current_scope.define(var)

    # define una funcion en el scope actual
    def define_function(self, func: FunctionSymbol):
        self.current_scope.define(func)

    # resuelve un simbolo desde el scope actual hacia arriba
    def resolve(self, name: str) -> Optional[Any]:
        return self.current_scope.resolve(name)