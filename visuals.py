import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def generate_heatmap(input: list[list[int]]):
    data = np.array([x for x in input])

    plt.figure(figsize=(10, 6))
    sns.heatmap(data, annot=False, fmt=".1f", cmap="viridis", cbar_kws={'label': 'Value'})


    plt.title("Heatmap of Lists with Averages Highlighted")
    plt.xlabel("Index")
    plt.ylabel("List Number")
    plt.show()
