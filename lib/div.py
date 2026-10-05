def div(a, b):
    """Divide a by b."""
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b
