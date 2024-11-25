def sevens(n, k):
    """Return the (clockwise) position of who says n among k players.

    >>> sevens(2, 5)
    2
    >>> sevens(6, 5)
    1
    >>> sevens(7, 5)
    2
    >>> sevens(8, 5)
    1
    >>> sevens(9, 5)
    5
    >>> sevens(18, 5)
    2
    """
    def f(i, who, direction):
        if i == n:
            return who
        "*** YOUR CODE HERE ***"
        i += 1
        if direction == 1:
            if who >= k:
                who = 1
            else:
                who += 1
        else:
            if who <= 1:
                who = k
            else:
                who -= 1
        if has_seven(i) == True or i % 7 == 0:
            direction = 1 - direction
        return f(i, who, direction)
    return f(1, 1, 1)

def has_seven(n):
    if n == 0:
        return False
    elif n % 10 == 7:
        return True
    else:
        return has_seven(n // 10)
    ##我tm熬了30分钟，结果是这一块不包括检验7的倍数，吐了