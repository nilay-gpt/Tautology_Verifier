from tautology import PropositionStatement


if __name__ == '__main__':
    """
    i/p example:
    "(!a | (a & a)), (!a | (b & !a)), (!a | a), ((a & (!b | b)) | (!a & (!b | b)))"
    """
    print "Enter the comma seperated boolean expr:"
    try:
        bool_expr = input()
        input_list = bool_expr.split(',')
        for expr in input_list:
            propostionStatement = PropositionStatement(expr)
            if propostionStatement.is_tautology():
                print "True"
            else:
                print "False"
    except SyntaxError as e:
        print "Error in input", e.message
