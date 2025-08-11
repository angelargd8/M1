# Generated from SimpleLang.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SimpleLangParser import SimpleLangParser
else:
    from SimpleLangParser import SimpleLangParser

# This class defines a complete generic visitor for a parse tree produced by SimpleLangParser.

class SimpleLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SimpleLangParser#prog.
    def visitProg(self, ctx:SimpleLangParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#assign.
    def visitAssign(self, ctx:SimpleLangParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#printExpr.
    def visitPrintExpr(self, ctx:SimpleLangParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#blank.
    def visitBlank(self, ctx:SimpleLangParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#Float.
    def visitFloat(self, ctx:SimpleLangParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#UnarySign.
    def visitUnarySign(self, ctx:SimpleLangParser.UnarySignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#Bool.
    def visitBool(self, ctx:SimpleLangParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#MulDiv.
    def visitMulDiv(self, ctx:SimpleLangParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#AddSub.
    def visitAddSub(self, ctx:SimpleLangParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#Var.
    def visitVar(self, ctx:SimpleLangParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#Parens.
    def visitParens(self, ctx:SimpleLangParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#Pow.
    def visitPow(self, ctx:SimpleLangParser.PowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#String.
    def visitString(self, ctx:SimpleLangParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#Int.
    def visitInt(self, ctx:SimpleLangParser.IntContext):
        return self.visitChildren(ctx)



del SimpleLangParser