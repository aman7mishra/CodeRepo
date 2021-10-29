"""
Factorial
"""

def fact(number):
    """
    Find the factorial of a number
    """
    if number == 2:
        return 2
    return number * fact(number - 1)

print(fact(5))
