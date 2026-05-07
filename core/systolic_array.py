import numpy as np
import math


class SystolicArray:

    def __init__(self, rows=4, cols=4):

        self.rows = rows
        self.cols = cols

        self.total_cycles = 0
        self.total_mac_operations = 0

    def execute_tile(self, A_tile, B_tile):

        A_tile = np.array(A_tile)
        B_tile = np.array(B_tile)

        M, K = A_tile.shape
        K, N = B_tile.shape

        C_tile = np.matmul(A_tile, B_tile)

        macs = M * K * N

        # 🔥 PARALLEL EXECUTION MODEL
        parallel_units = self.rows * self.cols

        cycles = math.ceil(macs / parallel_units)

        self.total_mac_operations += macs
        self.total_cycles += cycles

        return {
            "output": C_tile,
            "cycles": cycles,
            "macs": macs
        }

    def utilization(self):

        theoretical_peak = (
            self.rows *
            self.cols *
            self.total_cycles
        )

        if theoretical_peak == 0:
            return 0

        util = (
            self.total_mac_operations /
            theoretical_peak
        ) * 100

        return round(util, 2)
