import numpy as np


class Person:

    """
    :sizes: (int, int,)
    """
    def __init__(self, id, sizes):
        self.id = id
        self.x = sizes[0]
        self.y = sizes[1]

        # Create a random matrix image
        self.data = 255 * np.random.random((self.x, self.y))
        self.score = 0
    
    def get_avg(self):
        return np.sum(self.data) / (self.x * self.y)

    def __getitem__(self, i):
        return self.data[i]

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return "<Person: id={}, avg={}>".format(self.id, self.get_avg())
