import numpy as np


def sample_photon_positions(
    x,
    probability_density,
    n_photons,
    rng=None
):
    """
    Generate photon detection positions by random sampling
    from a normalized probability density.

    Parameters
    ----------
    x : array_like
        Screen position grid (m).
    probability_density : array_like
        Probability density evaluated on the position grid.
    n_photons : int
        Number of photons to detect.
    rng : numpy.random.Generator, optional
        Random number generator for reproducibility.

    Returns
    -------
    numpy.ndarray
        Simulated photon detection positions (m).
    """

    x = np.asarray(x, dtype=float)
    probability_density = np.asarray(
        probability_density,
        dtype=float
    )

    if x.ndim != 1 or probability_density.ndim != 1:
        raise ValueError("Input arrays must be one-dimensional.")

    if len(x) != len(probability_density) or len(x) < 2:
        raise ValueError("Input arrays must have equal length.")

    if not np.all(np.isfinite(x)) or not np.all(
        np.isfinite(probability_density)
    ):
        raise ValueError("Input arrays must contain finite values.")

    if np.any(np.diff(x) <= 0):
        raise ValueError("Position grid must be strictly increasing.")

    if np.any(probability_density < 0):
        raise ValueError("Probability density cannot be negative.")

    if not isinstance(n_photons, (int, np.integer)) or n_photons < 0:
        raise ValueError("Number of photons must be a non-negative integer.")

    if rng is None:
        rng = np.random.default_rng()

    # Calculate probability mass between adjacent grid points.
    dx = np.diff(x)

    segment_probability = (
        0.5
        * (probability_density[:-1] + probability_density[1:])
        * dx
    )

    cumulative_probability = np.concatenate(
        ([0.0], np.cumsum(segment_probability))
    )

    total_probability = cumulative_probability[-1]

    if total_probability <= 0:
        raise ValueError("Total probability must be positive.")

    # Normalize the cumulative distribution.
    cumulative_probability /= total_probability

    # Generate uniformly distributed random numbers.
    random_values = rng.random(n_photons)

    # Sample detection positions using inverse transform sampling.
    detection_positions = np.interp(
        random_values,
        cumulative_probability,
        x
    )

    return detection_positions
