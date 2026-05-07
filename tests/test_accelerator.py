import numpy as np

from core.systolic_array import SystolicArray


def test_matrix_multiplication():

    A = np.array([
        [1, 2],
        [3, 4]
    ])

    B = np.array([
        [5, 6],
        [7, 8]
    ])

    accelerator = SystolicArray(
        rows=2,
        cols=2
    )

    result = accelerator.execute_tile(A, B)

    expected = np.matmul(A, B)

    assert np.array_equal(
        result["output"],
        expected
    )

    print("✅ Accelerator test passed")


if __name__ == "__main__":
    test_matrix_multiplication()