# Generated from Gramatica.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GramaticaParser import GramaticaParser
else:
    from GramaticaParser import GramaticaParser

# This class defines a complete listener for a parse tree produced by GramaticaParser.
class GramaticaListener(ParseTreeListener):

    # Enter a parse tree produced by GramaticaParser#prog.
    def enterProg(self, ctx:GramaticaParser.ProgContext):
        pass

    # Exit a parse tree produced by GramaticaParser#prog.
    def exitProg(self, ctx:GramaticaParser.ProgContext):
        pass


    # Enter a parse tree produced by GramaticaParser#printExpr.
    def enterPrintExpr(self, ctx:GramaticaParser.PrintExprContext):
        pass

    # Exit a parse tree produced by GramaticaParser#printExpr.
    def exitPrintExpr(self, ctx:GramaticaParser.PrintExprContext):
        pass


    # Enter a parse tree produced by GramaticaParser#assign.
    def enterAssign(self, ctx:GramaticaParser.AssignContext):
        pass

    # Exit a parse tree produced by GramaticaParser#assign.
    def exitAssign(self, ctx:GramaticaParser.AssignContext):
        pass


    # Enter a parse tree produced by GramaticaParser#blank.
    def enterBlank(self, ctx:GramaticaParser.BlankContext):
        pass

    # Exit a parse tree produced by GramaticaParser#blank.
    def exitBlank(self, ctx:GramaticaParser.BlankContext):
        pass


    # Enter a parse tree produced by GramaticaParser#parens.
    def enterParens(self, ctx:GramaticaParser.ParensContext):
        pass

    # Exit a parse tree produced by GramaticaParser#parens.
    def exitParens(self, ctx:GramaticaParser.ParensContext):
        pass


    # Enter a parse tree produced by GramaticaParser#MulDiv.
    def enterMulDiv(self, ctx:GramaticaParser.MulDivContext):
        pass

    # Exit a parse tree produced by GramaticaParser#MulDiv.
    def exitMulDiv(self, ctx:GramaticaParser.MulDivContext):
        pass


    # Enter a parse tree produced by GramaticaParser#AddSub.
    def enterAddSub(self, ctx:GramaticaParser.AddSubContext):
        pass

    # Exit a parse tree produced by GramaticaParser#AddSub.
    def exitAddSub(self, ctx:GramaticaParser.AddSubContext):
        pass


    # Enter a parse tree produced by GramaticaParser#unaryMinus.
    def enterUnaryMinus(self, ctx:GramaticaParser.UnaryMinusContext):
        pass

    # Exit a parse tree produced by GramaticaParser#unaryMinus.
    def exitUnaryMinus(self, ctx:GramaticaParser.UnaryMinusContext):
        pass


    # Enter a parse tree produced by GramaticaParser#id.
    def enterId(self, ctx:GramaticaParser.IdContext):
        pass

    # Exit a parse tree produced by GramaticaParser#id.
    def exitId(self, ctx:GramaticaParser.IdContext):
        pass


    # Enter a parse tree produced by GramaticaParser#int.
    def enterInt(self, ctx:GramaticaParser.IntContext):
        pass

    # Exit a parse tree produced by GramaticaParser#int.
    def exitInt(self, ctx:GramaticaParser.IntContext):
        pass


