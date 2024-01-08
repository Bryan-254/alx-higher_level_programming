#!/usr/bin/python3
"""
My integer task
"""


class MyInt(int):
    """
    class MyInt that inherits from int
    """

    def __eq__(self, other):
        """
        The __eq__ method in Python is used to define
        the behavior of the equality operator (==)

        __eq__ is overridden to call the parent class's
        __ne__ method (super().__ne__(other)), essentially
        swapping the behavior of equality (==) with inequality (!=).
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        The __ne__ method in Python is used to define
        the behavior of the inequality operator (!=).

        __ne__ is overridden to call the parent class's
        __eq__ method (super().__eq__(other)), essentially
        swapping the behavior of inequality (!=) with equality (==).
        """
        return super().__eq__(other)
