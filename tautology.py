
from utils import infix_to_postfix, postfix_to_expression_tree, is_operand
from constants import Constants


class PropositionStatement(object):
    def __init__(self, statement):
        """
        This creates a proposition statement object
        Args:
        statement - this has to be a valid infix statement no validation is
        done
        """
        self.statement = statement

    def getVariableMap(self, statement):
        variableMap = dict()
        uniqueVaraibles = True
        for e in statement:
            if is_operand(e):
                if e in variableMap:
                    uniqueVaraibles = False
                else:
                    variableMap[e] = 0
        return (variableMap, uniqueVaraibles)

    def evaluateExprTree(self, root, variableMap):
        """
        This function evaulates the expression using expression
        tree
        Some optimization over postfix evaluation using expression
        tree
        """
        if root:
            value = root.data
            if is_operand(value):
                return variableMap[value]
            left = self.evaluateExprTree(root.left, variableMap)
            if value == Constants.NOT:
                return not left
            elif value == Constants.AND and not left:
                return False
            elif value == Constants.OR and left:
                return True
            right = self.evaluateExprTree(root.right, variableMap)
            if value == Constants.AND:
                return left and right
            elif value == Constants.OR:
                return left or right
            return True
        return True

    def is_tautology(self):
        """
        Determines whether a statement given is a tuatology or not

        Returns:
        This function returns whether a given statement is tautology or not
        """
        (variableMap, uniqueVaraibles) = self.getVariableMap(self.statement)
        # optimization step is that if all are unique variables, it won't be tautology
        if uniqueVaraibles:
            return False
        numVariables = len(variableMap)
        postfix = infix_to_postfix(self.statement)
        root = postfix_to_expression_tree(postfix)

        for i in range(pow(2, numVariables)):
            for e in enumerate(variableMap):
                offset = e[0]
                key = e[1]
                variableMap[key] = (i & (1 << offset)) >> offset
            if not self.evaluateExprTree(root, variableMap):
                return False
        return True
