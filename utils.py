
from constants import Constants


class TreeNode(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __str__(self):
        return " " + str(self.data) + " "

    def in_traversal(self):
        if self.left:
            self.left.in_traversal()
        if self.right:
            self.right.in_traversal()


def is_operand(char):
    "this will allow to accept the input in any case."
    return (char >= 'A' and char <= 'Z') or (char >= 'a' and char <= 'z')


def postfix_to_expression_tree(postfix):
    tree_list = list()
    for char in postfix:
        node = TreeNode(char)
        if char in Constants.OPERATORS:
            if char == Constants.NOT:
                node.left = tree_list.pop()
            else:
                node.right = tree_list.pop()
                node.left = tree_list.pop()
        tree_list.append(node)
    root = tree_list.pop()
    return root


def infix_to_postfix(infix):
    """
    convert infix expression to postfix expression
    """
    top = -1
    operatorstack = list()
    postfix = str()
    for char in infix:
        if char in Constants.OPERATORS:
            if char == Constants.CLOSE_BRACKET:
                while operatorstack:
                    operator = operatorstack.pop()
                    top -= 1
                    if operator == Constants.OPEN_BRACKET:
                        break
                    postfix += operator
            else:
                temp_top = top
                if char == Constants.OPEN_BRACKET:
                    operatorstack.append(char)
                else:
                    while temp_top > -1:
                        if operatorstack[temp_top] == Constants.OPEN_BRACKET:
                            break
                        if Constants.PRECEDENCE[operatorstack[top]] >= Constants.PRECEDENCE[char]:
                            postfix += str(operatorstack.pop())
                            top -= 1
                        temp_top -= 1
                    operatorstack.append(char)
                top += 1
        elif is_operand(char):
            postfix += char
    while operatorstack:
        postfix += str(operatorstack.pop())
        top -= 1
    return postfix
