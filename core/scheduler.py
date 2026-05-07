import numpy as np


class TileScheduler:
    def __init__(self, tile_size=2):
        self.tile_size = tile_size

    def generate_tiles(self, A, B):
        """
        Generate tiled workloads
        """

        A = np.array(A)
        B = np.array(B)

        M, K = A.shape
        K, N = B.shape

        tasks = []

        for i in range(0, M, self.tile_size):
            for j in range(0, N, self.tile_size):
                for k in range(0, K, self.tile_size):

                    A_tile = A[
                        i:i+self.tile_size,
                        k:k+self.tile_size
                    ]

                    B_tile = B[
                        k:k+self.tile_size,
                        j:j+self.tile_size
                    ]

                    tasks.append({
                        "A_tile": A_tile,
                        "B_tile": B_tile,
                        "position": (i, j)
                    })

        return tasks
