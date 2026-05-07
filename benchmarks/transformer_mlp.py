import numpy as np


def transformer_ffn():

    # Feed-forward network workload
    A = np.random.randint(0, 5, (256, 512))

    B = np.random.randint(0, 5, (512, 256))

    return A, B


def attention_projection():

    A = np.random.randint(0, 5, (128, 768))

    B = np.random.randint(0, 5, (768, 128))

    return A, B