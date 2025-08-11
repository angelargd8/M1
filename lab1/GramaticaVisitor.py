# Generated from Gramatica.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GramaticaParser import GramaticaParser
else:
    from GramaticaParser import GramaticaParser

# This class defines a complete generic visitor for a parse tree produced by GramaticaParser.

class GramaticaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GramaticaParser#prog.
    def visitProg(self, ctx:GramaticaParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#printExpr.
    def visitPrintExpr(self, ctx:GramaticaParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#assign.
    def visitAssign(self, ctx:GramaticaParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#blank.
    def visitBlank(self, ctx:GramaticaParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#parens.
    def visitParens(self, ctx:GramaticaParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#MulDiv.
    def visitMulDiv(self, ctx:GramaticaParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#AddSub.
    def visitAddSub(self, ctx:GramaticaParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#unaryMinus.
    def visitUnaryMinus(self, ctx:GramaticaParser.UnaryMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#id.
    def visitId(self, ctx:GramaticaParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#int.
    def visitInt(self, ctx:GramaticaParser.IntContext):
        return self.visitChildren(ctx)



del GramaticaParser