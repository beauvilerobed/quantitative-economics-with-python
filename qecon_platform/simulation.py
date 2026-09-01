"""

Simulation utilities for the Quantitative Economics Platform.

"""
from typing import Tuple
import numpy as np


def simulate_ornstein_uhlenbeck(
    theta: float = 0.5,
    mu: float = 0.0,
    sigma: float = 0.1,
    x0: float = 0.0,
    dt: float = 1e-2,
    T: float = 1.0,
    n_paths: int = 1,
) -> Tuple[np.ndarray, np.ndarray]:
    """Simulate Ornstein–Uhlenbeck processes.

    Returns time grid and an array of shape (n_steps+1, n_paths).
    """
    n_steps = int(np.ceil(T / dt))
    t = np.linspace(0.0, n_steps * dt, n_steps + 1)
    paths = np.empty((n_steps + 1, n_paths), dtype=float)
    paths[0] = x0
    sqrt_dt = np.sqrt(dt)

    for i in range(1, n_steps + 1):
        dw = np.random.normal(scale=sqrt_dt, size=n_paths)
        paths[i] = (
            paths[i - 1]
            + theta * (mu - paths[i - 1]) * dt
            + sigma * dw
        )

    return t, paths


def simulate_agent_micro(
    n_agents: int = 100,
    n_steps: int = 100,
    prob_trade: float = 0.1,
    init_wealth: float = 1.0,
) -> np.ndarray:
    """A minimal agent-based microeconomic simulation.

    Each agent has a scalar `wealth`. At each step, with probability
    `prob_trade` an agent is paired with another random agent and they trade a
    small fraction of wealth. This function returns an array shape
    (n_steps+1, n_agents) with wealth over time.
    """
    wealth = np.full((n_steps + 1, n_agents), float(init_wealth))

    for t in range(1, n_steps + 1):
        wealth[t] = wealth[t - 1].copy()
        traders = np.where(np.random.rand(n_agents) < prob_trade)[0]
        np.random.shuffle(traders)
        # pair traders two-by-two
        for i in range(0, len(traders) - 1, 2):
            a = traders[i]
            b = traders[i + 1]
            # simple transfer: a fraction of average wealth
            frac = 0.05 * np.random.rand()
            transfer = frac * 0.5 * (wealth[t, a] + wealth[t, b])
            wealth[t, a] -= transfer
            wealth[t, b] += transfer

    return wealth
