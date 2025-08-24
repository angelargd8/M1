from dataclasses import dataclass
from typing import List, Optional, Union, Any

@dataclass
class Program:
    decls: List[Any]

@dataclass
class VarDecl:
    name: str
    type: str
    is_const : bool = False
    init: Optional[Any] = None

@dataclass
class Param:
    name: str
    type: str

@dataclass
class FuncDecl:
    name: str
    params: List[Param]
    return_type: str
    body: List[Any]

@dataclass
class ClassDecl:
    name: str
    methods: List[FuncDecl]
    properties: List[VarDecl]

# ------------------ sentencias --------------------
@dataclass
class Block:
    statements: List[Any]

@dataclass
class Assign: 
    name: str
    expr: Any

@dataclass
class If: 
    condition: Any
    then_branch: Any
    else_branch: Optional[Any] = None

@dataclass
class While: 
    condition: Any
    body: Any

@dataclass
class For: 
    init: Optional[Any] = None
    condition: Any
    step : Optional[Any] = None
    body: Any

@dataclass
class Return: 
    expresion: Optional[Any] = None


@dataclass
class Break: 
    pass

@dataclass
class Continue: 
    pass

# -------------------- expresiones ---------------------

@dataclass
class Var:
    name: str
    type: str

    @dataclass
    class Call: 
        func: str
        args: List[Any]

    @dataclass
    class Member: 
        object: Any
        name: str

    @dataclass
    class Index: 
        seq: Any
        index: Any

    @dataclass
    class UnOp: 
        op: str
        expr: Any

    @dataclass
    class BinOp: 
        left: Any
        op: str
        right: Any


# -------- Literales ---------


@dataclass
class IntLiteral: 
    value: int

@dataclass
class StringLiteral: 
    value: str

@dataclass
class BooleanLiteral: 
    value: bool

@dataclass
class NullLiteral: 
    pass

@dataclass
class FloatLiteral: 
    value: float

@dataclass
class ListLiteral: 
    elements: List[Any]
