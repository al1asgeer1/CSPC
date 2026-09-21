# CSPC Lab A
## PW1 — Lab A

**Speed comparison (200000 atoms, 200 steps):**
- Pure-Python loop: 2.668 s
- NumPy: 0.000296 s
- Speed-up: about 9000x

**Tests:** all 3 tests pass (`pytest -v`).

**Conclusion:** The NumPy version is much faster because it decides
all atoms at once with one vectorised binomial draw, while the loop
checks every atom one by one in slow Python code.
**Conclusion:** The NumPy version was about 9000 times faster than the
pure-Python loop. The loop checks every atom one by one in slow Python
code, while NumPy decides all atoms at once with a single vectorised
binomial draw. Both versions follow the same physics, and the tests
confirm that the average decay matches N0 * exp(-lam * t).