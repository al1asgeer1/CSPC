# CSPC
## PW1 --- Lab B

The observed decay data followed the same overall exponential shape
as the analytical decay law N0 * e^(-λt), with λ = 0.3. The two
curves matched closely, confirming that the observed counts decay
consistently with the theoretical exponential model. The Snakemake
pipeline automates the figure generation: it reruns `plot.py` only
when `decay_observed.csv` or `plot.py` change, and does nothing when
the output is already up to date.
## PW2 --- Lab A

- **Mean acceleration:** ... (öz rəqəmin)
- **Why the acceleration was noisy:** Each derivative divides small measurement errors by the small time step, so differentiating twice amplifies the noise.
- **Integrating back:** Integrating the noisy acceleration twice recovered the position to within X m, because integration accumulates values and random noise partly cancels out.

![motion](PW2/Lab%20A/motion.png)
