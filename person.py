import numpy as np


class Person:

    """
    :sizes: (int, int,)
    """
    def __init__(self, id, sizes):
        self.id = id
        self.x = sizes[0]
        self.y = sizes[1]
        self.data = list(255*np.random.random((self.x, self.y)))  # Numbers must be between 0 and 1
        self.score = 0
    
    def get_avg(self):
        return np.sum(self.data) / (self.x * self.y)

    def __str__(self):
        avg = self.get_avg()
        return "<Person: id={}, avg={}>".format(self.id, avg)
