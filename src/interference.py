import numpy as np


def calculate_single_slit_amplitude(
    x,
    wavelength,
    screen_distance,
    slit_width
):
    """
    Calculate the single-slit Fraunhofer diffraction amplitude.
    """

    u = (
        np.pi * slit_width * x
        / (wavelength * screen_distance)
    )

    return np.sinc(u / np.pi)


def calculate_double_slit_amplitude(
    x,
    wavelength,
    screen_distance,
    slit_width,
    slit_separation
):
    """
    Calculate the coherent double-slit amplitude.
    """

    single_slit = calculate_single_slit_amplitude(
        x,
        wavelength,
        screen_distance,
        slit_width
    )

    phase = (
        np.pi * slit_separation * x
        / (wavelength * screen_distance)
    )

    return 2.0 * single_slit * np.cos(phase)


def calculate_intensity(
    x,
    wavelength,
    screen_distance,
    slit_width,
    slit_separation
):
    """
    Calculate the double-slit interference intensity.
    """

    amplitude = calculate_double_slit_amplitude(
        x,
        wavelength,
        screen_distance,
        slit_width,
        slit_separation
    )

    return np.abs(amplitude) ** 2


def calculate_probability_density(
    x,
    wavelength,
    screen_distance,
    slit_width,
    slit_separation
):
    """
    Calculate the normalized photon detection probability density.
    """

    x = np.asarray(x, dtype=float)

    if x.ndim != 1 or len(x) < 2:
        raise ValueError(
            "At least two screen positions are required."
        )

    if not np.all(np.isfinite(x)):
        raise ValueError(
            "Screen positions must be finite."
        )

    if np.any(np.diff(x) <= 0):
        raise ValueError(
            "Screen positions must be strictly increasing."
        )

    intensity = calculate_intensity(
        x,
        wavelength,
        screen_distance,
        slit_width,
        slit_separation
    )

    normalization = np.trapezoid(intensity, x)

    if not np.isfinite(normalization) or normalization <= 0:
        raise ValueError(
            "Intensity normalization must be positive."
        )

    return intensity / normalization
