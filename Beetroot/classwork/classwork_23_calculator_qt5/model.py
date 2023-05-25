def evaluateExpression(expression):

    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = "Error"

    return result
