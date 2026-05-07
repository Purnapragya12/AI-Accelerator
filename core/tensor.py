import numpy as np


class Tensor:
    def __init__(self, data):
        self.data = np.array(data)

    @property
    def shape(self):
        return self.data.shape

    def __repr__(self):
        return f"Tensor(shape={self.shape})"
