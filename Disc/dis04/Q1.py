def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
#    def helper(m, n):
#        if m == 1 or n == 1:
#            return 1
#        else:
#            return helper(m - 1, n) + helper(m, n - 1)
#    return helper(m, n)

    def helper(m, n):
        if m == 1 or n == 1:
            return 1
        else:
            result = helper(m - 1, n) + helper(m, n - 1)
            return result
    return helper(m, n)