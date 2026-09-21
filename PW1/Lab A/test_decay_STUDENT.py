"""
Tests for the decay simulation.

One complete test is given as a model. Add the two tests described in the
lab handout (a negative-rate test, and a test against the analytical law).
Run with:  pytest -v
"""

import numpy as np
import pytest
from decay import simulate, simulate_loop


def test_starts_at_N0():
    # at time zero, no atoms have decayed yet
    assert simulate(1000, 0.4)[0] == 1000


# TODO 1: test_rejects_negative_rate
#   Check that calling simulate(...) with a negative lam raises a ValueError.
#   Which pytest tool checks that an error is raised?


# TODO 2: test_matches_law
#   Check that the simulation's AVERAGE over many seeds is close to the
#   physical law  N0 * exp(-lam * t).
#   Which pytest tool compares floating-point values with a tolerance?

def test_rejects_negative_rate():
    # mənfi lam ValueError verməlidir
    with pytest.raises(ValueError):
        simulate(1000, -0.4)


def test_matches_law():
    # çox seed üzrə orta nəticə N0*exp(-lam*t)-yə yaxın olmalıdır
    N0, lam, dt, steps = 10000, 0.4, 0.05, 50
    runs = [simulate(N0, lam, dt, steps, seed=s) for s in range(20)]
    mean_final = np.mean([r[-1] for r in runs])
    expected = N0 * np.exp(-lam * dt * steps)
    assert mean_final == pytest.approx(expected, rel=0.05)