from SimpleLangListener import SimpleLangListener
from SimpleLangParser import SimpleLangParser
from custom_types import IntType, FloatType, StringType, BoolType, UnknownType

def type_name(t):
    return t.__class__.__name__

class TypeCheckListener(SimpleLangListener):
    def __init__(self):
        self.errors = []
        self.env = {}     # variables: nombre -> tipo (instancia) #instacia =('int','float','bool','string','unknown')  
        self.types = {}   # ctx -> tipo (instancia) 

    # ----- Primarios / literales -----
    def exitInt(self, ctx: SimpleLangParser.IntContext):
        self.types[ctx] = IntType()

    def exitFloat(self, ctx: SimpleLangParser.FloatContext):
        self.types[ctx] = FloatType()

    def exitString(self, ctx: SimpleLangParser.StringContext):
        self.types[ctx] = StringType()

    def exitBool(self, ctx: SimpleLangParser.BoolContext):
        self.types[ctx] = BoolType()

    def exitParens(self, ctx: SimpleLangParser.ParensContext):
        self.types[ctx] = self.types.get(ctx.expr(), UnknownType())

    def exitVar(self, ctx: SimpleLangParser.VarContext):
        name = ctx.ID().getText()
        t = self.env.get(name)
        if t is None:
            self.errors.append(f"Variable '{name}' usada antes de asignación")
            t = UnknownType()
        self.types[ctx] = t

    # ----- Asignación -----
    def exitAssign(self, ctx: SimpleLangParser.AssignContext):
        t = self.types.get(ctx.expr(), UnknownType())
        name = ctx.ID().getText()
        self.env[name] = t

    # ----- Unario (+x, -x) -----
    def exitUnarySign(self, ctx: SimpleLangParser.UnarySignContext):
        t = self.types.get(ctx.expr(), UnknownType())
        op = ctx.op.text
        if isinstance(t, (IntType, FloatType)):
            self.types[ctx] = t
        else:
            self.errors.append(f"Operador unario '{op}' no aplicable a tipo {type_name(t)}")
            self.types[ctx] = UnknownType()

    # ----- Binarios -----
    def _numeric_result(self, lt, rt):
        # promoción simple
        if isinstance(lt, UnknownType) or isinstance(rt, UnknownType):
            return UnknownType()
        if isinstance(lt, (IntType, FloatType)) and isinstance(rt, (IntType, FloatType)):
            return FloatType() if isinstance(lt, FloatType) or isinstance(rt, FloatType) else IntType()
        return None  # inválido

    def exitMulDiv(self, ctx: SimpleLangParser.MulDivContext):
        lt = self.types.get(ctx.expr(0), UnknownType())
        rt = self.types.get(ctx.expr(1), UnknownType())
        res = self._numeric_result(lt, rt)
        if res is None:
            self.errors.append(
                f"Unsupported operand types for {ctx.op.text}: {type_name(lt)} and {type_name(rt)}"
            )
            res = UnknownType()
        self.types[ctx] = res

    def exitAddSub(self, ctx: SimpleLangParser.AddSubContext):
        lt = self.types.get(ctx.expr(0), UnknownType())
        rt = self.types.get(ctx.expr(1), UnknownType())
        if ctx.op.text == '+':
            #permitir concatenación:
            if isinstance(lt, StringType) and isinstance(rt, StringType):
                self.types[ctx] = StringType()
                return
        res = self._numeric_result(lt, rt)
        if res is None:
            self.errors.append(
                f"Unsupported operand types for {ctx.op.text}: {type_name(lt)} and {type_name(rt)}"
            )
            res = UnknownType()
        self.types[ctx] = res

    def exitPow(self, ctx: SimpleLangParser.PowContext):
        lt = self.types.get(ctx.expr(0), UnknownType())
        rt = self.types.get(ctx.expr(1), UnknownType())
        if isinstance(lt, (IntType, FloatType)) and isinstance(rt, (IntType, FloatType)):
            # muchas implementaciones devuelven float
            self.types[ctx] = FloatType() if isinstance(lt, FloatType) or isinstance(rt, FloatType) else IntType()
        else:
            self.errors.append(
                f"Potencia inválida entre {type_name(lt)} y {type_name(rt)}"
            )
            self.types[ctx] = UnknownType()
