import numpy as np

from core.systolic_array import SystolicArray
from core.memory_controller import MemoryController
from core.scheduler import TileScheduler
from core.metrics import PerformanceMetrics

# Matrix size
SIZE = 8

A = np.random.randint(0, 10, (SIZE, SIZE))
B = np.random.randint(0, 10, (SIZE, SIZE))

accelerator = SystolicArray(rows=4, cols=4)

memory = MemoryController(
    sram_size_kb=256,
    bandwidth_gb_per_sec=32
)

scheduler = TileScheduler(tile_size=4)

metrics = PerformanceMetrics()

tasks = scheduler.generate_tiles(A, B)

C = np.zeros((SIZE, SIZE))

for task in tasks:

    A_tile = task["A_tile"]
    B_tile = task["B_tile"]

    # Simulate memory fetch
    memory.access_data(size_kb=64)

    # Execute tile
    result = accelerator.execute_tile(
        A_tile,
        B_tile
    )

    C_tile = result["output"]

    metrics.update(
        result["cycles"],
        result["macs"]
    )

    i, j = task["position"]

    C[
        i:i+C_tile.shape[0],
        j:j+C_tile.shape[1]
    ] += C_tile

print("\n===== AI Accelerator Simulation =====\n")

print("Matrix Size:", SIZE, "x", SIZE)

print("\nOutput Matrix:")
print(C)

print("\n===== PERFORMANCE =====")

summary = metrics.summary()

for k, v in summary.items():
    print(f"{k}: {v}")

print("\nUtilization:")
print(f"{accelerator.utilization()}%")

print("\n===== MEMORY =====")

memory_stats = memory.stats()

for k, v in memory_stats.items():
    print(f"{k}: {v}")
