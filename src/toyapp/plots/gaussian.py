# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt


def g(x, mu, sigma):
    """ gaussian function """
    return 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-((x - mu) / sigma) ** 2 / 2)


def gaussian_plot(mu=0, sigma=1, npts=100, fig=None):
    """ Return a gaussian sample points """

    if fig is None:
        fig, (ax1, ax2) = plt.subplots(
            nrows=2, sharex=True,
            gridspec_kw=dict(hspace=0, height_ratios=[1, 4]))

    # draw data:
    xr = np.random.normal(mu, sigma, npts)
    x = np.linspace(mu - 6 * sigma, mu + 6 * sigma, 100)

    ax1.boxplot(xr, vert=False)
    ax1.set_yticks([])
    ax1.set_title(fr"$\mu$ = {mu:.1f} $\sigma$ = {sigma:.1f}")
    ax2.plot(x, g(x, mu, sigma), color="C3")
    ax2.hist(xr, rwidth=.8, density=True, color="C0", alpha=.25)
    ax2.set_ylabel("Distribution")
    ax2.set_xlabel("Random variable")

    fig.suptitle("Normal distribution")

    return fig


def color_plot(color):
    """ plot according to the color """

    x = np.random.normal(0, 1, 100)

    fig, ax = plt.subplots()

    ax.plot(x, color=color)
    ax.set_title("Title")
    ax.set_xlabel("x label")
    ax.set_ylabel("y label")

    return fig
