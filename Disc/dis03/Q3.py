def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    
    def helper(i):
        if i == 1:
            return True
        if n % i == 0:
            return False
        else:
            return helper(i - 1)
    return helper(n-1)