def swipe(n):
    """Print the digits of n, one per line, first backward then forward.

    >>> swipe(2837)
    7
    3
    8
    2
    8
    3
    7
    """
    if n < 10:
        print(n)
    else:
        "*** YOUR CODE HERE ***"
        print(n % 10)
        ##这个是来的时候打印的
        swipe(n // 10)
        print(n % 10)
        ##这个是swipe回去的时候打印的