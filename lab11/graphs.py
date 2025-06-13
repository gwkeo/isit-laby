import matplotlib.pyplot as plt
import numpy as np

def plot_adaptive(data, msgID):
    plt.figure(figsize=(10, 6))

    if len(data) < 20:
        plt.plot(data, marker='o', linestyle='-', linewidth=1, markersize=5)
    elif len(data) < 100:
        plt.plot(data, linestyle='-', linewidth=1)
    else:
        plt.plot(data, linewidth=0.5)
    
    plt.title('Курс валют')
    plt.xlabel('Индекс точки')
    plt.ylabel('Значение')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    filename = str(msgID) + ".png"
    plt.savefig(filename, dpi=100,bbox_inches="tight")
    plt.close()

    return filename