
from utils import infix_to_postfix, postfix_to_expression_tree, is_operand
from constants import Constants


class PropositionStatement(object):
    def __init__(self, statement):
        """
        This creates a statement object
        Args:
        statement- expression and no validation is done in expresion is valid or not.
        """
        self.statement = statement

    def get_variable_map(self, statement):
        variable_map = dict()
        unique_varaibles = True
        for char in statement:
            if is_operand(char):
                if char in variable_map:
                    unique_varaibles = False
                else:
                    variable_map[char] = 0
        return (variable_map, unique_varaibles)

    def evaluate_expression_tree(self, root, variable_map):
        """
        This function evaulates the expression using expression
        tree
        """
        if root:
            value = root.data
            if is_operand(value):
                return variable_map[value]
            left = self.evaluate_expression_tree(root.left, variable_map)
            if value == Constants.NOT:
                return not left
            elif value == Constants.AND and not left:
                return False
            elif value == Constants.OR and left:
                return True
            right = self.evaluate_expression_tree(root.right, variable_map)
            if value == Constants.AND:
                return left and right
            elif value == Constants.OR:
                return left or right
            return True
        return True

    def is_tautology(self):
        """
        Returns:
        This function returns whether a given statement is tautology or not
        Boolean: True/False
        """
        (variable_map, unique_varaibles) = self.get_variable_map(self.statement)
        postfix = infix_to_postfix(self.statement)
        root = postfix_to_expression_tree(postfix)

        for value in range(pow(2, len(variable_map))):
            for element in enumerate(variable_map):
                offset = element[0]
                key = element[1]
                variable_map[key] = (value & (1 << offset)) >> offset
            if not self.evaluate_expression_tree(root, variable_map):
                return False
        return True
