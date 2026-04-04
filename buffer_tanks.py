import numpy as np


def calc_amplitude_response(omega, tau_h, n):
    """Calculate the amplitude ratio of n buffer tanks in series.

    Arguments
    ----------
    omega : float
        Angular frequency (rad/min).
    tau_h : float
        Total residence time of system (min).
    n : int
        Number of buffer tanks in series.
    """
    return 1 / (1 + (omega * tau_h / n) ** 2) ** (n / 2)


def calc_phase_response(omega, tau_h, n):
    """Calculate the phase response of n buffer tanks in series.

    Arguments
    ----------
    omega : float
        Angular frequency (rad/min).
    tau_h : float
        Total residence time of system (min).
    n : int
        Number of buffer tanks in series.
    """
    return -n * np.arctan(omega * tau_h)
