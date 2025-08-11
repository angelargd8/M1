# Generated from SimpleLang.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SimpleLangParser import SimpleLangParser
else:
    from SimpleLangParser import SimpleLangParser

# This class defines a complete listener for a parse tree produced by SimpleLangParser.
class SimpleLangListener(ParseTreeListener):

    # Enter a parse tree produced by SimpleLangParser#prog.
    def enterProg(self, ctx:SimpleLangParser.ProgContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#prog.
    def exitProg(self, ctx:SimpleLangParser.ProgContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#assign.
    def enterAssign(self, ctx:SimpleLangParser.AssignContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#assign.
    def exitAssign(self, ctx:SimpleLangParser.AssignContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#printExpr.
    def enterPrintExpr(self, ctx:SimpleLangParser.PrintExprContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#printExpr.
    def exitPrintExpr(self, ctx:SimpleLangParser.PrintExprContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#blank.
    def enterBlank(self, ctx:SimpleLangParser.BlankContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#blank.
    def exitBlank(self, ctx:SimpleLangParser.BlankContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#Float.
    def enterFloat(self, ctx:SimpleLangParser.FloatContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#Float.
    def exitFloat(self, ctx:SimpleLangParser.FloatContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#UnarySign.
    def enterUnarySign(self, ctx:SimpleLangParser.UnarySignContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#UnarySign.
    def exitUnarySign(self, ctx:SimpleLangParser.UnarySignContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#Bool.
    def enterBool(self, ctx:SimpleLangParser.BoolContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#Bool.
    def exitBool(self, ctx:SimpleLangParser.BoolContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#MulDiv.
    def enterMulDiv(self, ctx:SimpleLangParser.MulDivContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#MulDiv.
    def exitMulDiv(self, ctx:SimpleLangParser.MulDivContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#AddSub.
    def enterAddSub(self, ctx:SimpleLangParser.AddSubContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#AddSub.
    def exitAddSub(self, ctx:SimpleLangParser.AddSubContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#Var.
    def enterVar(self, ctx:SimpleLangParser.VarContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#Var.
    def exitVar(self, ctx:SimpleLangParser.VarContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#Parens.
    def enterParens(self, ctx:SimpleLangParser.ParensContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#Parens.
    def exitParens(self, ctx:SimpleLangParser.ParensContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#Pow.
    def enterPow(self, ctx:SimpleLangParser.PowContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#Pow.
    def exitPow(self, ctx:SimpleLangParser.PowContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#String.
    def enterString(self, ctx:SimpleLangParser.StringContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#String.
    def exitString(self, ctx:SimpleLangParser.StringContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#Int.
    def enterInt(self, ctx:SimpleLangParser.IntContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#Int.
    def exitInt(self, ctx:SimpleLangParser.IntContext):
        pass


