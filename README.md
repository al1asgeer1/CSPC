# CSPC
## PW1 --- Lab B

The observed decay data followed the same overall exponential shape
as the analytical decay law N0 * e^(-λt), with λ = 0.3. The two
curves matched closely, confirming that the observed counts decay
consistently with the theoretical exponential model. The Snakemake
pipeline automates the figure generation: it reruns `plot.py` only
when `decay_observed.csv` or `plot.py` change, and does nothing when
the output is already up to date.