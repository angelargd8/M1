from dataclasses import dataclass, field
from typing import Dict, Optional, Any, List

# tabla de simbolo por alcance
# estructura de datos que guarda informacion de los nombres de las variables que hay en un lenguaje de programacion

@dataclass
class TypeSymbol:
    name: str


@dataclass
class VariableSymbol:
    name: str
    type: TypeSymbol
    const: bool = False
    initialized: bool = False
    decl_node: Any = None
    line: int = -1
    col: int = -1

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

class Scope: 
    def __init__(self, name: str, parent: Optional['Scope'] = None):
        self.name = name
        self.parent = parent
        self.symbols: Dict[str, Any] = {}  # puede contener VariableSymbol o FunctionSymbol

    def define(self, sym):
        if sym.name in self.symbols:
            raise Exception(f"Error: '{sym.name}' ya está definido en este alcance.")
        self.symbols[sym.name] = sym

    def resolve(self, name: str) -> Optional[Any]:
        if name in self.symbols:
            return self.symbols[name]
        if self.parent:
            return self.parent.resolve(name)
        return None

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
    
    def push_scope(self, name: str):
        self.current_scope = Scope(name, self.current_scope)
        return self.current_scope
    
    def pop_scope(self):
        if self.current_scope.parent is None:
            raise Exception("Error: No se puede salir del alcance global.")
        self.current_scope = self.current_scope.parent

    def get_type(self, name: str) -> TypeSymbol:
        t = self.types.get(name)
        if t:
            return t
        # soporte arreglos: int[], int[][]
        if name.endswith("]"):
            # normaliza todo lo que termine en [] como 'list'
            return self.types["list"]
        raise Exception(f"Error: Tipo '{name}' no definido.")

    def exit_scope(self):
        if self.current_scope.parent is not None:
            self.current_scope = self.current_scope.parent
        else:
            raise Exception("Error: No se puede salir del alcance global.")

    def define_variable(self, var: VariableSymbol):
        self.current_scope.define(var)

    def define_function(self, func: FunctionSymbol):
        self.current_scope.define(func)

    def resolve(self, name: str) -> Optional[Any]:
        return self.current_scope.resolve(name)