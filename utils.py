
from treeNode import TreeNode
from constants import Constants


def is_operand(s):
    "this will take the input in caps as well as in small also."
    return (s >= 'A' and s <= 'Z') or (s >= 'a' and s <= 'z')


def postfix_to_expression_tree(postfix):
    exprTreeStack = []
    for e in postfix:
        node = TreeNode(e)
        if e in Constants.OPERATORS:
            if e == Constants.NOT:
                node.left = exprTreeStack.pop()
            else:
                node.right = exprTreeStack.pop()
                node.left = exprTreeStack.pop()
        exprTreeStack.append(node)
    root = exprTreeStack.pop()
    return root


def infix_to_postfix(infix):
    """
    convert infix expression to postfix expression
    """
    top = -1
    operatorstack = []
    postfix = ''
    for s in infix:
        if s in Constants.OPERATORS:
            if s == Constants.CLOSE_BRACKET:
                while operatorstack:
                    op = operatorstack.pop()
                    top -= 1
                    if op == Constants.OPEN_BRACKET:
                        break
                    postfix += op
            else:
                temp_top = top
                if s == Constants.OPEN_BRACKET:
                    operatorstack.append(s)
                else:
                    while temp_top > -1:
                        if operatorstack[temp_top] == Constants.OPEN_BRACKET:
                            break
                        if Constants.PRECEDENCE[operatorstack[top]] >= Constants.PRECEDENCE[s]:
                            postfix += str(operatorstack.pop())
                            top -= 1
                        temp_top -= 1
                    operatorstack.append(s)
                top += 1
        elif is_operand(s):
            postfix += s
    while operatorstack:
        postfix += str(operatorstack.pop())
        top -= 1
    return postfix


def evaluateExpr(postfix, variableMap):
    """
        This function expects statement to be postfix expression with
        values of variables map to variableMap dictionary and it calculates
        the given expression is true or false based on the values of
        variableMap

    @postfix - the input statement has to be postfix expression
    @variableMap - the variables mapped values
    """
    resultStack = []
    for e in postfix:
        if is_operand(e):
            resultStack.append(e)
        elif e in Constants.OPERATORS:
            if e == Constants.NOT:
                val = resultStack.pop()
                if isinstance(val, type('str')):
                    val = variableMap[val]
                resultStack.append(not val)
            elif e == Constants.AND:
                valA = resultStack.pop()
                valB = resultStack.pop()
                if isinstance(valA, type('str')):
                    valA = variableMap[valA]
                if isinstance(valB, type('str')):
                    valB = variableMap[valB]
                resultStack.append(valA and valB)
            elif e == Constants.OR:
                valA = resultStack.pop()
                valB = resultStack.pop()
                if isinstance(valA, type('str')):
                    valA = variableMap[valA]
                if isinstance(valB, type('str')):
                    valB = variableMap[valB]
                resultStack.append(valA or valB)
    result = resultStack.pop()
    if isinstance(result, type('str')):
        result = variableMap[result]
    return result


def evaluateExprTree(root, variableMap):
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
        left = evaluateExprTree(root.left, variableMap)
        if value == Constants.NOT:
            return not left
        elif value == Constants.AND and not left:
            return False
        elif value == Constants.OR and left:
            return True
        right = evaluateExprTree(root.right, variableMap)
        if value == Constants.AND:
            return left and right
        elif value == Constants.OR:
            return left or right
        return True
    return True
