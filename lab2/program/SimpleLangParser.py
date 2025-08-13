# Generated from SimpleLang.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\24")
        buf.write("9\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\7\2\13\n\2\f\2\16\2")
        buf.write("\16\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5")
        buf.write("\3\33\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\5\4)\n\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4")
        buf.write("\64\n\4\f\4\16\4\67\13\4\3\4\2\3\6\5\2\4\6\2\5\3\3\20")
        buf.write("\20\3\2\5\6\3\2\7\t\2B\2\f\3\2\2\2\4\32\3\2\2\2\6(\3\2")
        buf.write("\2\2\b\13\5\4\3\2\t\13\7\20\2\2\n\b\3\2\2\2\n\t\3\2\2")
        buf.write("\2\13\16\3\2\2\2\f\n\3\2\2\2\f\r\3\2\2\2\r\17\3\2\2\2")
        buf.write("\16\f\3\2\2\2\17\20\7\2\2\3\20\3\3\2\2\2\21\22\7\22\2")
        buf.write("\2\22\23\7\3\2\2\23\24\5\6\4\2\24\25\t\2\2\2\25\33\3\2")
        buf.write("\2\2\26\27\5\6\4\2\27\30\t\2\2\2\30\33\3\2\2\2\31\33\7")
        buf.write("\20\2\2\32\21\3\2\2\2\32\26\3\2\2\2\32\31\3\2\2\2\33\5")
        buf.write("\3\2\2\2\34\35\b\4\1\2\35\36\t\3\2\2\36)\5\6\4\13\37)")
        buf.write("\7\f\2\2 )\7\r\2\2!)\7\16\2\2\")\7\17\2\2#)\7\22\2\2$")
        buf.write("%\7\n\2\2%&\5\6\4\2&\'\7\13\2\2\')\3\2\2\2(\34\3\2\2\2")
        buf.write("(\37\3\2\2\2( \3\2\2\2(!\3\2\2\2(\"\3\2\2\2(#\3\2\2\2")
        buf.write("($\3\2\2\2)\65\3\2\2\2*+\f\f\2\2+,\7\4\2\2,\64\5\6\4\f")
        buf.write("-.\f\n\2\2./\t\4\2\2/\64\5\6\4\13\60\61\f\t\2\2\61\62")
        buf.write("\t\3\2\2\62\64\5\6\4\n\63*\3\2\2\2\63-\3\2\2\2\63\60\3")
        buf.write("\2\2\2\64\67\3\2\2\2\65\63\3\2\2\2\65\66\3\2\2\2\66\7")
        buf.write("\3\2\2\2\67\65\3\2\2\2\b\n\f\32(\63\65")
        return buf.getvalue()


class SimpleLangParser ( Parser ):

    grammarFileName = "SimpleLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'^'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "INT", "FLOAT", "STRING", 
                      "BOOL", "NEWLINE", "WS", "ID", "LINE_COMMENT", "BLOCK_COMMENT" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2

    ruleNames =  [ "prog", "stat", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    INT=10
    FLOAT=11
    STRING=12
    BOOL=13
    NEWLINE=14
    WS=15
    ID=16
    LINE_COMMENT=17
    BLOCK_COMMENT=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SimpleLangParser.EOF, 0)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.StatContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.StatContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleLangParser.NEWLINE)
            else:
                return self.getToken(SimpleLangParser.NEWLINE, i)

        def getRuleIndex(self):
            return SimpleLangParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = SimpleLangParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimpleLangParser.T__2) | (1 << SimpleLangParser.T__3) | (1 << SimpleLangParser.T__7) | (1 << SimpleLangParser.INT) | (1 << SimpleLangParser.FLOAT) | (1 << SimpleLangParser.STRING) | (1 << SimpleLangParser.BOOL) | (1 << SimpleLangParser.NEWLINE) | (1 << SimpleLangParser.ID))) != 0):
                self.state = 8
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 6
                    self.stat()
                    pass

                elif la_ == 2:
                    self.state = 7
                    self.match(SimpleLangParser.NEWLINE)
                    pass


                self.state = 12
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 13
            self.match(SimpleLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SimpleLangParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BlankContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(SimpleLangParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlank" ):
                listener.enterBlank(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlank" ):
                listener.exitBlank(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlank" ):
                return visitor.visitBlank(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(SimpleLangParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(SimpleLangParser.NEWLINE, 0)
        def EOF(self):
            return self.getToken(SimpleLangParser.EOF, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)


    class PrintExprContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(SimpleLangParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(SimpleLangParser.NEWLINE, 0)
        def EOF(self):
            return self.getToken(SimpleLangParser.EOF, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintExpr" ):
                listener.enterPrintExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintExpr" ):
                listener.exitPrintExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintExpr" ):
                return visitor.visitPrintExpr(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = SimpleLangParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        self._la = 0 # Token type
        try:
            self.state = 24
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = SimpleLangParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.match(SimpleLangParser.ID)
                self.state = 16
                self.match(SimpleLangParser.T__0)
                self.state = 17
                self.expr(0)
                self.state = 18
                _la = self._input.LA(1)
                if not(_la==SimpleLangParser.EOF or _la==SimpleLangParser.NEWLINE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                localctx = SimpleLangParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.expr(0)
                self.state = 21
                _la = self._input.LA(1)
                if not(_la==SimpleLangParser.EOF or _la==SimpleLangParser.NEWLINE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 3:
                localctx = SimpleLangParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 23
                self.match(SimpleLangParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SimpleLangParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class FloatContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(SimpleLangParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat" ):
                return visitor.visitFloat(self)
            else:
                return visitor.visitChildren(self)


    class UnarySignContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(SimpleLangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnarySign" ):
                listener.enterUnarySign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnarySign" ):
                listener.exitUnarySign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnarySign" ):
                return visitor.visitUnarySign(self)
            else:
                return visitor.visitChildren(self)


    class BoolContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL(self):
            return self.getToken(SimpleLangParser.BOOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool" ):
                listener.enterBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool" ):
                listener.exitBool(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool" ):
                return visitor.visitBool(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class VarContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(SimpleLangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class PowContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPow" ):
                listener.enterPow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPow" ):
                listener.exitPow(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPow" ):
                return visitor.visitPow(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(SimpleLangParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(SimpleLangParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpleLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SimpleLangParser.T__2, SimpleLangParser.T__3]:
                localctx = SimpleLangParser.UnarySignContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 27
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==SimpleLangParser.T__2 or _la==SimpleLangParser.T__3):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 28
                self.expr(9)
                pass
            elif token in [SimpleLangParser.INT]:
                localctx = SimpleLangParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 29
                self.match(SimpleLangParser.INT)
                pass
            elif token in [SimpleLangParser.FLOAT]:
                localctx = SimpleLangParser.FloatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 30
                self.match(SimpleLangParser.FLOAT)
                pass
            elif token in [SimpleLangParser.STRING]:
                localctx = SimpleLangParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 31
                self.match(SimpleLangParser.STRING)
                pass
            elif token in [SimpleLangParser.BOOL]:
                localctx = SimpleLangParser.BoolContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 32
                self.match(SimpleLangParser.BOOL)
                pass
            elif token in [SimpleLangParser.ID]:
                localctx = SimpleLangParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 33
                self.match(SimpleLangParser.ID)
                pass
            elif token in [SimpleLangParser.T__7]:
                localctx = SimpleLangParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 34
                self.match(SimpleLangParser.T__7)
                self.state = 35
                self.expr(0)
                self.state = 36
                self.match(SimpleLangParser.T__8)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 51
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 49
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = SimpleLangParser.PowContext(self, SimpleLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 40
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 41
                        self.match(SimpleLangParser.T__1)
                        self.state = 42
                        self.expr(10)
                        pass

                    elif la_ == 2:
                        localctx = SimpleLangParser.MulDivContext(self, SimpleLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 43
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 44
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimpleLangParser.T__4) | (1 << SimpleLangParser.T__5) | (1 << SimpleLangParser.T__6))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 45
                        self.expr(9)
                        pass

                    elif la_ == 3:
                        localctx = SimpleLangParser.AddSubContext(self, SimpleLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 46
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 47
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==SimpleLangParser.T__2 or _la==SimpleLangParser.T__3):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 48
                        self.expr(8)
                        pass

             
                self.state = 53
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         




