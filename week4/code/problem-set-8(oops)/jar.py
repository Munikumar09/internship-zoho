class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Invalid capacity")
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        if n+self.size > self.capacity:
            raise ValueError("Exceeds Jar capacity")
        self.size += n

    def withdraw(self, n):
        if self.size-n < 0:
            raise ValueError("Insufficient Cookies")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @size.setter
    def size(self, size):
        self._size = size
jar = Jar(20)
print(jar)
jar.deposit(10)
print(jar)