def factorial(n):
    """
    Calculate the factorial of a number.

    Args:
        n (int): The number to calculate the factorial of.

    Returns:
        int: The factorial of the input number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
