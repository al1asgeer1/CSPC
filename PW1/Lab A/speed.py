import time
from decay import simulate, simulate_loop

N0, lam = 200000, 0.4

start = time.perf_counter()
simulate_loop(N0, lam)
t_loop = time.perf_counter() - start

start = time.perf_counter()
simulate(N0, lam)
t_numpy = time.perf_counter() - start

print(f"Loop : {t_loop:.3f} s")
print(f"NumPy: {t_numpy:.3f} s")
print(f"NumPy version is {t_loop / t_numpy:.0f}x faster")
print(f"Loop : {t_loop:.4f} s")
print(f"NumPy: {t_numpy:.6f} s")