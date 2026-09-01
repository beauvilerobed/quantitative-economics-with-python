"""qecon_platform

Small interactive platform helpers for quantitative economics simulations.
"""
from .simulation import simulate_ornstein_uhlenbeck, simulate_agent_micro

__all__ = [
    "simulate_ornstein_uhlenbeck",
    "simulate_agent_micro",
]
