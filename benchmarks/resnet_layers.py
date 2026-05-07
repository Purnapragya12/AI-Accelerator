import numpy as np


def conv_layer_benchmark():

    # Simulate convolution GEMM lowering
    A = np.random.randint(0, 5, (64, 128))

    B = np.random.randint(0, 5, (128, 64))

    return A, B


def bottleneck_block():

    A = np.random.randint(0, 5, (128, 256))

    B = np.random.randint(0, 5, (256, 128))

    return A, B