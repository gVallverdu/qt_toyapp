# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

def color_plot(color):
    """ plot according to the color """

    x = np.random.normal(0, 1, 100)

    fig, ax = plt.subplots()

    ax.plot(x, color=color)
    ax.set_title(f"Color plot: {color}")
    ax.set_xlabel("x label")
    ax.set_ylabel("y label")

    return fig