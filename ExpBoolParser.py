# Generated from ExpBool.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write(".\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\27\n\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\7\3\"\n\3\f\3\16\3%\13\3\3\4\3")
        buf.write("\4\7\4)\n\4\f\4\16\4,\13\4\3\4\2\3\4\5\2\4\6\2\4\3\2\n")
        buf.write("\13\3\2\n\f\2\60\2\b\3\2\2\2\4\26\3\2\2\2\6&\3\2\2\2\b")
        buf.write("\t\5\6\4\2\t\n\7\3\2\2\n\13\5\4\3\2\13\3\3\2\2\2\f\r\b")
        buf.write("\3\1\2\r\27\5\6\4\2\16\17\7\7\2\2\17\20\5\4\3\2\20\21")
        buf.write("\7\b\2\2\21\27\3\2\2\2\22\23\7\t\2\2\23\24\5\4\3\2\24")
        buf.write("\25\7\b\2\2\25\27\3\2\2\2\26\f\3\2\2\2\26\16\3\2\2\2\26")
        buf.write("\22\3\2\2\2\27#\3\2\2\2\30\31\f\7\2\2\31\32\7\4\2\2\32")
        buf.write("\"\5\4\3\b\33\34\f\6\2\2\34\35\7\5\2\2\35\"\5\4\3\7\36")
        buf.write("\37\f\5\2\2\37 \7\6\2\2 \"\5\4\3\6!\30\3\2\2\2!\33\3\2")
        buf.write("\2\2!\36\3\2\2\2\"%\3\2\2\2#!\3\2\2\2#$\3\2\2\2$\5\3\2")
        buf.write("\2\2%#\3\2\2\2&*\t\2\2\2\')\t\3\2\2(\'\3\2\2\2),\3\2\2")
        buf.write("\2*(\3\2\2\2*+\3\2\2\2+\7\3\2\2\2,*\3\2\2\2\6\26!#*")
        return buf.getvalue()


class ExpBoolParser ( Parser ):

    grammarFileName = "ExpBool.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':='", "'and'", "'or'", "'xor'", "'not('", 
                     "')'", "'('", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "' '" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "LOWERCASEE", "UPPERCASEE", "INT", "WHITESPACE" ]

    RULE_funtion = 0
    RULE_exp = 1
    RULE_variable = 2

    ruleNames =  [ "funtion", "exp", "variable" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    LOWERCASEE=8
    UPPERCASEE=9
    INT=10
    WHITESPACE=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class FuntionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExpBoolParser.RULE_funtion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FunctionBoolContext(FuntionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExpBoolParser.FuntionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def variable(self):
            return self.getTypedRuleContext(ExpBoolParser.VariableContext,0)

        def exp(self):
            return self.getTypedRuleContext(ExpBoolParser.ExpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionBool" ):
                listener.enterFunctionBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionBool" ):
                listener.exitFunctionBool(self)



    def funtion(self):

        localctx = ExpBoolParser.FuntionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_funtion)
        try:
            localctx = ExpBoolParser.FunctionBoolContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.variable()
            self.state = 7
            self.match(ExpBoolParser.T__0)
            self.state = 8
            self.exp(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExpBoolParser.RULE_exp

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class OpNOTContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExpBoolParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exp(self):
            return self.getTypedRuleContext(ExpBoolParser.ExpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpNOT" ):
                listener.enterOpNOT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpNOT" ):
                listener.exitOpNOT(self)


    class VariableBoolContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExpBoolParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def variable(self):
            return self.getTypedRuleContext(ExpBoolParser.VariableContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableBool" ):
                listener.enterVariableBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableBool" ):
                listener.exitVariableBool(self)


    class OpXorContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExpBoolParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpBoolParser.ExpContext)
            else:
                return self.getTypedRuleContext(ExpBoolParser.ExpContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpXor" ):
                listener.enterOpXor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpXor" ):
                listener.exitOpXor(self)


    class IntoMarksContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExpBoolParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exp(self):
            return self.getTypedRuleContext(ExpBoolParser.ExpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntoMarks" ):
                listener.enterIntoMarks(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntoMarks" ):
                listener.exitIntoMarks(self)


    class OpANDDContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExpBoolParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpBoolParser.ExpContext)
            else:
                return self.getTypedRuleContext(ExpBoolParser.ExpContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpANDD" ):
                listener.enterOpANDD(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpANDD" ):
                listener.exitOpANDD(self)


    class OpORRContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExpBoolParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpBoolParser.ExpContext)
            else:
                return self.getTypedRuleContext(ExpBoolParser.ExpContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpORR" ):
                listener.enterOpORR(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpORR" ):
                listener.exitOpORR(self)



    def exp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExpBoolParser.ExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_exp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ExpBoolParser.LOWERCASEE, ExpBoolParser.UPPERCASEE]:
                localctx = ExpBoolParser.VariableBoolContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 11
                self.variable()
                pass
            elif token in [ExpBoolParser.T__4]:
                localctx = ExpBoolParser.OpNOTContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 12
                self.match(ExpBoolParser.T__4)
                self.state = 13
                self.exp(0)
                self.state = 14
                self.match(ExpBoolParser.T__5)
                pass
            elif token in [ExpBoolParser.T__6]:
                localctx = ExpBoolParser.IntoMarksContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 16
                self.match(ExpBoolParser.T__6)
                self.state = 17
                self.exp(0)
                self.state = 18
                self.match(ExpBoolParser.T__5)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 33
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 31
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = ExpBoolParser.OpANDDContext(self, ExpBoolParser.ExpContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 22
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 23
                        self.match(ExpBoolParser.T__1)
                        self.state = 24
                        self.exp(6)
                        pass

                    elif la_ == 2:
                        localctx = ExpBoolParser.OpORRContext(self, ExpBoolParser.ExpContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 25
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 26
                        self.match(ExpBoolParser.T__2)
                        self.state = 27
                        self.exp(5)
                        pass

                    elif la_ == 3:
                        localctx = ExpBoolParser.OpXorContext(self, ExpBoolParser.ExpContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 28
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 29
                        self.match(ExpBoolParser.T__3)
                        self.state = 30
                        self.exp(4)
                        pass

             
                self.state = 35
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOWERCASEE(self, i:int=None):
            if i is None:
                return self.getTokens(ExpBoolParser.LOWERCASEE)
            else:
                return self.getToken(ExpBoolParser.LOWERCASEE, i)

        def UPPERCASEE(self, i:int=None):
            if i is None:
                return self.getTokens(ExpBoolParser.UPPERCASEE)
            else:
                return self.getToken(ExpBoolParser.UPPERCASEE, i)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(ExpBoolParser.INT)
            else:
                return self.getToken(ExpBoolParser.INT, i)

        def getRuleIndex(self):
            return ExpBoolParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)




    def variable(self):

        localctx = ExpBoolParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            _la = self._input.LA(1)
            if not(_la==ExpBoolParser.LOWERCASEE or _la==ExpBoolParser.UPPERCASEE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 40
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 37
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExpBoolParser.LOWERCASEE) | (1 << ExpBoolParser.UPPERCASEE) | (1 << ExpBoolParser.INT))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 42
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.exp_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp_sempred(self, localctx:ExpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         




