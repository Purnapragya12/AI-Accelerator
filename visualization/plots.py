import matplotlib.pyplot as plt
import numpy as np


def plot_performance(metrics):

    labels = [
        "Cycles",
        "MACs",
        "TOPS"
    ]

    values = [
        metrics["cycles"],
        metrics["macs"],
        metrics["tops"]
    ]

    fig, ax = plt.subplots(figsize=(6, 4))

    ax.bar(labels, values)

    ax.set_title("Accelerator Performance")

    return fig



def plot_memory(memory_stats):

    labels = [
        "SRAM Hits",
        "DRAM Accesses",
        "Memory Stalls"
    ]

    values = [
        memory_stats["sram_hits"],
        memory_stats["dram_accesses"],
        memory_stats["memory_stalls"]
    ]

    fig, ax = plt.subplots(figsize=(6, 4))

    ax.bar(labels, values)

    ax.set_title("Memory Hierarchy")

    return fig



def plot_utilization_gauge(utilization):

    fig, ax = plt.subplots(figsize=(6, 1.8))

    ax.barh([0], [utilization])

    ax.set_xlim(0, 100)

    ax.set_title("MAC Utilization")

    ax.set_xlabel("Percent")

    return fig



def plot_heatmap(matrix):

    fig, ax = plt.subplots(figsize=(6, 6))

    heatmap = ax.imshow(matrix)

    ax.set_title("Output Matrix Heatmap")

    plt.colorbar(heatmap)

    return fig
