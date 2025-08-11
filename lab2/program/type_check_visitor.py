from SimpleLangParser import SimpleLangParser
from SimpleLangVisitor import SimpleLangVisitor
from custom_types import IntType, FloatType, StringType, BoolType, UnknownType

def type_name(t):
    return t.__class__.__name__

class TypeCheckVisitor(SimpleLangVisitor):
    def __init__(self, allow_string_plus=False):
        self.env = {}      # nombre -> tipo (instancia)
        self.errors = []   # lista de strings
        self.allow_string_plus = allow_string_plus

    # ----- Helpers -----
    def _numeric_result(self, lt, rt):
        # promoción simple: int op float -> float; int op int -> int
        if isinstance(lt, UnknownType) or isinstance(rt, UnknownType):
            return UnknownType()
        if isinstance(lt, (IntType, FloatType)) and isinstance(rt, (IntType, FloatType)):
            return FloatType() if isinstance(lt, FloatType) or isinstance(rt, FloatType) else IntType()
        return None  # inválido

    # ===== Reglas de 'stat' etiquetadas =====
    def visitAssign(self, ctx: SimpleLangParser.AssignContext):
        t = self.visit(ctx.expr())
        name = ctx.ID().getText()
        self.env[name] = t
        return t

    def visitPrintExpr(self, ctx: SimpleLangParser.PrintExprContext):
        # Solo chequea tipos de la expresión
        return self.visit(ctx.expr())

    def visitBlank(self, ctx: SimpleLangParser.BlankContext):
        return None

    # ===== Reglas de 'expr' etiquetadas =====
    def visitInt(self, ctx: SimpleLangParser.IntContext):
        return IntType()

    def visitFloat(self, ctx: SimpleLangParser.FloatContext):
        return FloatType()

    def visitString(self, ctx: SimpleLangParser.StringContext):
        return StringType()

    def visitBool(self, ctx: SimpleLangParser.BoolContext):
        return BoolType()

    def visitParens(self, ctx: SimpleLangParser.ParensContext):
        return self.visit(ctx.expr())

    def visitVar(self, ctx: SimpleLangParser.VarContext):
        name = ctx.ID().getText()
        t = self.env.get(name)
        if t is None:
            self.errors.append(f"Variable '{name}' usada antes de asignación")
            return UnknownType()
        return t

    def visitUnarySign(self, ctx: SimpleLangParser.UnarySignContext):
        t = self.visit(ctx.expr())
        op = ctx.op.text
        if isinstance(t, (IntType, FloatType)):
            return t
        self.errors.append(f"Operador unario '{op}' no aplicable a tipo {type_name(t)}")
        return UnknownType()

    def visitMulDiv(self, ctx: SimpleLangParser.MulDivContext):
        lt = self.visit(ctx.expr(0))
        rt = self.visit(ctx.expr(1))
        res = self._numeric_result(lt, rt)
        if res is None:
            self.errors.append(
                f"Unsupported operand types for {ctx.op.text}: {type_name(lt)} and {type_name(rt)}"
            )
            return UnknownType()
        return res

    def visitAddSub(self, ctx: SimpleLangParser.AddSubContext):
        lt = self.visit(ctx.expr(0))
        rt = self.visit(ctx.expr(1))
        if ctx.op.text == '+' and self.allow_string_plus:
            if isinstance(lt, StringType) and isinstance(rt, StringType):
                return StringType()
        res = self._numeric_result(lt, rt)
        if res is None:
            self.errors.append(
                f"Unsupported operand types for {ctx.op.text}: {type_name(lt)} and {type_name(rt)}"
            )
            return UnknownType()
        return res

    def visitPow(self, ctx: SimpleLangParser.PowContext):
        lt = self.visit(ctx.expr(0))
        rt = self.visit(ctx.expr(1))
        if isinstance(lt, (IntType, FloatType)) and isinstance(rt, (IntType, FloatType)):
            # muchas implementaciones devuelven float si hay un float en los operandos
            return FloatType() if isinstance(lt, FloatType) or isinstance(rt, FloatType) else IntType()
        self.errors.append(f"Potencia inválida entre {type_name(lt)} y {type_name(rt)}")
        return UnknownType()
