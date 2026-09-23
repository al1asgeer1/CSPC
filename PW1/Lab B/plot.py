import numpy as np
import matplotlib.pyplot as plt

# TODO 1: read decay_observed.csv into arrays t and observed
t, observed = np.loadtxt("decay_observed.csv", delimiter=",", skiprows=1, unpack=True)

# TODO 2: set N0 to the first observed value and build analytical
LAMBDA = 0.3
N0 = observed[0]
analytical = N0 * np.exp(-LAMBDA * t)

# TODO 3: 1x2 subplot with shared x and y axes
fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True)

ax1.scatter(t, observed)
ax1.set_title("Observed")
ax1.set_xlabel("time")
ax1.set_ylabel("count")

ax2.plot(t, analytical)
ax2.set_title("Analytical")
ax2.set_xlabel("time")
ax2.set_ylabel("count")

# TODO 4: save the figure as figure.png
plt.savefig("figure.png")