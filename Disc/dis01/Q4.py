def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    a = 0
    list1 = []
    for i in str(n):
        if i not in list1:
            list1.append(i)
    print(len(list1))

def has_digit(n, k):
    """Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert k >= 0 and k < 10
    found = False
    for i in str(n):
        if i == k:
            found = True
    if found:
        print("True")
    else:
        print("False")

