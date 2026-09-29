import numpy as np
import matplotlib
matplotlib.use("Agg")  # ekran olmayan mühitdə də işləsin
import matplotlib.pyplot as plt

# (a) 
data = np.genfromtxt("freefall.csv", delimiter=",", skip_header=1)
t = data[:, 0]   # time
y = data[:, 1]   # y (hündürlük, metr)

# (b) 
v = np.gradient(y, t)  
a = np.gradient(v, t)   

# (c) 
print("Mean acceleration:", np.mean(a))
print("Mean acceleration:", a.mean())
print("Std of acceleration:", a.std())
from scipy.integrate import cumulative_trapezoid

# a -> v
v_rec = cumulative_trapezoid(a, t, initial=0) + v[0]

# v_rec -> y
y_rec = cumulative_trapezoid(v_rec, t, initial=0) + y[0]


diff = np.abs(y_rec - y)
print("Largest difference:", diff.max())
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(8, 9))

ax1.plot(t, y)
ax1.set_ylabel("Position y (m)")

ax2.plot(t, v)
ax2.set_ylabel("Velocity v (m/s)")

ax3.plot(t, a, label="Acceleration (from data)")
ax3.axhline(-9.81, color="r", linestyle="--", label="-9.81 m/s²")
ax3.set_ylabel("Acceleration a (m/s²)")
ax3.set_xlabel("Time t (s)")
ax3.legend()

fig.tight_layout()
fig.savefig("motion.png", dpi=150)