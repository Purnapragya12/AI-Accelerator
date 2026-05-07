import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

import streamlit as st
import numpy as np
import pandas as pd

from core.systolic_array import SystolicArray
from core.memory_controller import MemoryController
from core.scheduler import TileScheduler
from core.metrics import PerformanceMetrics

from visualization.plots import (
    plot_performance,
    plot_memory,
    plot_utilization_gauge,
    plot_heatmap
)

# ================= PAGE CONFIG =================

st.set_page_config(
    page_title="AI Accelerator Simulator",
    layout="wide",
)

# ================= HEADER =================

st.title("AI Accelerator Simulator")

st.markdown("""
Interactive simulator for systolic-array based AI accelerators.

Simulates:
- Parallel matrix execution
- Tile scheduling
- SRAM-aware memory hierarchy
- Throughput and utilization metrics
""")

# ================= SIDEBAR =================

st.sidebar.header("⚙️ Accelerator Configuration")

matrix_size = st.sidebar.number_input(
    "Matrix Size",
    min_value=4,
    max_value=512,
    value=16,
    step=4
)

array_size = st.sidebar.number_input(
    "Systolic Array Size",
    min_value=2,
    max_value=64,
    value=4,
    step=2
)

tile_size = st.sidebar.number_input(
    "Tile Size",
    min_value=2,
    max_value=64,
    value=4,
    step=2
)

sram_size = st.sidebar.number_input(
    "SRAM Size (KB)",
    min_value=64,
    max_value=8192,
    value=256,
    step=64
)

# ================= MATRICES =================

A = np.random.randint(
    0,
    10,
    (matrix_size, matrix_size)
)

B = np.random.randint(
    0,
    10,
    (matrix_size, matrix_size)
)

# ================= COMPONENTS =================

accelerator = SystolicArray(
    rows=array_size,
    cols=array_size
)

memory = MemoryController(
    sram_size_kb=sram_size,
    bandwidth_gb_per_sec=32
)

scheduler = TileScheduler(
    tile_size=tile_size
)

metrics = PerformanceMetrics()

# ================= EXECUTION =================

tasks = scheduler.generate_tiles(A, B)

C = np.zeros((matrix_size, matrix_size))

for task in tasks:

    tile_memory = (
        (
            task["A_tile"].nbytes +
            task["B_tile"].nbytes
        ) / 1024
    ) * matrix_size

    memory.access_data(size_kb=tile_memory)

    result = accelerator.execute_tile(
        task["A_tile"],
        task["B_tile"]
    )

    metrics.update(
        result["cycles"],
        result["macs"]
    )

    C_tile = result["output"]

    i, j = task["position"]

    C[
        i:i+C_tile.shape[0],
        j:j+C_tile.shape[1]
    ] += C_tile

# ================= METRICS =================

summary = metrics.summary()

utilization = accelerator.utilization()

memory_stats = memory.stats()

# ================= TOP METRICS =================

st.header("Accelerator Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Cycles",
    summary["cycles"]
)

col2.metric(
    "MAC Operations",
    summary["macs"]
)

col3.metric(
    "TOPS",
    summary["tops"]
)

col4.metric(
    "Utilization (%)",
    utilization
)

# ================= CHARTS =================

st.header("Performance Analytics")

chart1, chart2 = st.columns(2)

with chart1:
    st.pyplot(
        plot_performance(summary)
    )

with chart2:
    st.pyplot(
        plot_memory(memory_stats)
    )

# ================= UTILIZATION =================

st.header("Compute Utilization")

st.pyplot(
    plot_utilization_gauge(utilization)
)

# ================= HEATMAP =================

st.header("Output Matrix Heatmap")

st.pyplot(
    plot_heatmap(C)
)

# ================= MATRICES =================

st.header("Matrix Data")

matrix_col1, matrix_col2 = st.columns(2)

with matrix_col1:
    st.subheader("Matrix A")
    st.dataframe(pd.DataFrame(A))

with matrix_col2:
    st.subheader("Matrix B")
    st.dataframe(pd.DataFrame(B))

st.subheader("Output Matrix")
st.dataframe(pd.DataFrame(C))

# ================= MEMORY =================

st.header("Memory Statistics")

memory_df = pd.DataFrame(
    list(memory_stats.items()),
    columns=["Metric", "Value"]
)

st.table(memory_df)

# ================= FOOTER =================

st.markdown("---")

st.markdown(
    "Built with Python, NumPy, Streamlit and custom accelerator simulation architecture."
)
