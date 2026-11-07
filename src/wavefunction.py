import numpy as np


def normalized_sinc(u):
    """
    Compute the normalized sinc function:
    sinc(u) = sin(u) / u, with sinc(0) = 1.
    """
    return np.sinc(u / np.pi)


def single_slit_amplitude(x, wavelength, screen_distance, slit_width):
    """
    Calculate the single-slit amplitude in the Fraunhofer regime.

    Parameters
    ----------
    x : array_like
        Position on the observation screen (m).
    wavelength : float
        Photon wavelength (m).
    screen_distance : float
        Distance between the slits and the screen (m).
    slit_width : float
        Width of each slit (m).

    Returns
    -------
    numpy.ndarray
        Single-slit amplitude envelope.
    """
    u = np.pi * slit_width * x / (wavelength * screen_distance)
    return normalized_sinc(u)


def double_slit_amplitude(
    x,
    wavelength,
    screen_distance,
    slit_width,
    slit_separation
):
    """
    Calculate the coherent double-slit amplitude.

    The two slits are assumed to have equal amplitudes
    and a relative phase determined by their separation.
    """
    envelope = single_slit_amplitude(
        x,
        wavelength,
        screen_distance,
        slit_width
    )

    phase = (
        np.pi * slit_separation * x
        / (wavelength * screen_distance)
    )

    return 2.0 * envelope * np.cos(phase)
