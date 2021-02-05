# Generated from ExpBool.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExpBoolParser import ExpBoolParser
else:
    from ExpBoolParser import ExpBoolParser

# This class defines a complete listener for a parse tree produced by ExpBoolParser.
class ExpBoolListener(ParseTreeListener):

    # Enter a parse tree produced by ExpBoolParser#functionBool.
    def enterFunctionBool(self, ctx:ExpBoolParser.FunctionBoolContext):
        pass

    # Exit a parse tree produced by ExpBoolParser#functionBool.
    def exitFunctionBool(self, ctx:ExpBoolParser.FunctionBoolContext):
        pass


    # Enter a parse tree produced by ExpBoolParser#opNOT.
    def enterOpNOT(self, ctx:ExpBoolParser.OpNOTContext):
        pass

    # Exit a parse tree produced by ExpBoolParser#opNOT.
    def exitOpNOT(self, ctx:ExpBoolParser.OpNOTContext):
        pass


    # Enter a parse tree produced by ExpBoolParser#variableBool.
    def enterVariableBool(self, ctx:ExpBoolParser.VariableBoolContext):
        pass

    # Exit a parse tree produced by ExpBoolParser#variableBool.
    def exitVariableBool(self, ctx:ExpBoolParser.VariableBoolContext):
        pass


    # Enter a parse tree produced by ExpBoolParser#opXor.
    def enterOpXor(self, ctx:ExpBoolParser.OpXorContext):
        pass

    # Exit a parse tree produced by ExpBoolParser#opXor.
    def exitOpXor(self, ctx:ExpBoolParser.OpXorContext):
        pass


    # Enter a parse tree produced by ExpBoolParser#intoMarks.
    def enterIntoMarks(self, ctx:ExpBoolParser.IntoMarksContext):
        pass

    # Exit a parse tree produced by ExpBoolParser#intoMarks.
    def exitIntoMarks(self, ctx:ExpBoolParser.IntoMarksContext):
        pass


    # Enter a parse tree produced by ExpBoolParser#opANDD.
    def enterOpANDD(self, ctx:ExpBoolParser.OpANDDContext):
        pass

    # Exit a parse tree produced by ExpBoolParser#opANDD.
    def exitOpANDD(self, ctx:ExpBoolParser.OpANDDContext):
        pass


    # Enter a parse tree produced by ExpBoolParser#opORR.
    def enterOpORR(self, ctx:ExpBoolParser.OpORRContext):
        pass

    # Exit a parse tree produced by ExpBoolParser#opORR.
    def exitOpORR(self, ctx:ExpBoolParser.OpORRContext):
        pass


    # Enter a parse tree produced by ExpBoolParser#variable.
    def enterVariable(self, ctx:ExpBoolParser.VariableContext):
        pass

    # Exit a parse tree produced by ExpBoolParser#variable.
    def exitVariable(self, ctx:ExpBoolParser.VariableContext):
        pass


