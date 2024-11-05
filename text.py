def middle(a, b, c):
    """Return the number among a, b, and c that is not the smallest or largest.
    Assume a, b, and c are all different numbers.

    >>> middle(3, 5, 4)
    4
    >>> middle(30, 5, 4)
    5
    >>> middle(3, 5, 40)
    5
    >>> middle(3, 5, 40)
    5
    >>> middle(30, 5, 40)
    30
    """
    return sorted([a,b,c])[1]
a,b,c = 2,6,5
assert middle(a,b,c) == 5, "haha,代码写错了555"

##可以打出python -m doctest -v text.py来用>>>里的公式检查。