"""Performs several simple math calculations.

This module helps users perform mathematical calculations.

Examples:
    >>> from calculator import calculations
    >>> calculations.add(2, 4)
    6.0
    >>> calculations.multiply(2.0, 5.0)
    10.0
    >>> from calculator.calculations import divide
    >>> divide(5.0, 2.5)
    2.0

The module performs the following operations:
- `add(a, b)` - returns the sum of two numbers.
- `subtract(a, b)` - returns the difference of two numbers.
- `multiply(a, b)` - returns the product of two numbers.
- `divide(a, b)` - returns the quotient of two numbers.
"""

from typing import Union

def add(a: Union[float, int], b: Union[float, int])-> float:
    """Compute and return the sum of two numbers.

    Examples:
        >>> add(2.0, 4.0)
        6.0
        >>> add(3.5, 7.1)
        10.6
    
    Args:
        a: A number representing the first addend in the addition.
        b: A number representing the second addend in the addition.

    Returns:
        A number representing the sum of 'a' and 'b'.
    """
    return float(a + b)

def subtract(a: Union[float, int], b: Union[float, int]):
    """Compute and return the difference between two numbers.
    
    Examples:
        >>> subtract(4.0, 3.0)
        1.0
        >>> subtract(3.2, 1.6)
        1.6

    Args:
        a: The minuend- number from which the other number is subtracted.
        b: the subtrahend- number to be subtracted from the minuend.

    Returns:
        A number representing the difference between 'a' and 'b'.
    """
    return float(a - b)

def multiply(a: Union[float, int], b: Union[float, int]):
    """Compute and return the multiplication of two numbers.
    
    Examples:
        >>> multiply(2.0, 4.0)
        8.0
        >>> multiply(3.0, 7.0)
        21.0

    Args:
        a: A number representing the first factor in the multiplication.
        b: A number representing the second factor in the multiplication.

    Returns:
        A number representing the product of 'a' and 'b'.
    """
    return float(a * b)

def divide(a: Union[float, int], b: Union[float, int]):
    """Compute and return the division between two numbers.
    
    Examples:
        >>> divide(4.0, 4.0)
        1.0
        >>> divide(3.6, 1.8)
        2.0
    
    Args:
        a: A number representing the dividend- number that is being divided.
        b: A number representing the divisor-  number that does the division.

    Returns:
        A number representing the quotient of 'a' and 'b'.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return float(a  / b)