class Jar:
    def __init__(self, capacity=12):
        # __init__ should initialize a cookie jar with the given capacity,
        # which represents the maximum number of cookies that can fit in the cookie jar.
        # If capacity is not a non-negative int, though, __init__ should instead raise a ValueError.
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        # __str__ should return a str with 🍪,
        # where is the number of cookies in the cookie jar.
        # For instance, if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"
        return "\U0001F36A" * self.size

    def deposit(self, n):
        self.n = n
        if self.size + n > self.capacity:
            raise ValueError
        self._size += self.n

    def withdraw(self, n):
        if self.size < n:
            raise ValueError
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
