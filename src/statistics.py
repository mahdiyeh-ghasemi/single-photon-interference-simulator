import numpy as np


def multinomial_counts(probabilities, n_photons, rng=None):
    """
    Generate photon counts using a multinomial distribution.

    Parameters
    ----------
    probabilities : array_like
        Probability of detection in each screen bin.
    n_photons : int
        Fixed total number of photons.
    rng : numpy.random.Generator, optional
        Random number generator.

    Returns
    -------
    numpy.ndarray
        Photon counts in each bin.
    """

    probabilities = np.asarray(probabilities, dtype=float)

    if probabilities.ndim != 1 or len(probabilities) == 0:
        raise ValueError("Probabilities must be a non-empty 1D array.")

    if not np.all(np.isfinite(probabilities)):
        raise ValueError("Probabilities must be finite.")

    if np.any(probabilities < 0):
        raise ValueError("Probabilities cannot be negative.")

    if not isinstance(n_photons, (int, np.integer)) or n_photons < 0:
        raise ValueError("Number of photons must be a non-negative integer.")

    total = probabilities.sum()

    if total <= 0:
        raise ValueError("Total probability must be positive.")

    probabilities = probabilities / total

    if rng is None:
        rng = np.random.default_rng()

    return rng.multinomial(n_photons, probabilities)


def poisson_counts(mean_counts, rng=None):
    """
    Generate photon counts using independent Poisson distributions.

    Parameters
    ----------
    mean_counts : array_like
        Expected photon count in each screen bin.
    rng : numpy.random.Generator, optional
        Random number generator.

    Returns
    -------
    numpy.ndarray
        Simulated photon counts in each bin.
    """

    mean_counts = np.asarray(mean_counts, dtype=float)

    if mean_counts.ndim != 1:
        raise ValueError("Mean counts must be a 1D array.")

    if not np.all(np.isfinite(mean_counts)):
        raise ValueError("Mean counts must be finite.")

    if np.any(mean_counts < 0):
        raise ValueError("Mean counts cannot be negative.")

    if rng is None:
        rng = np.random.default_rng()

    return rng.poisson(mean_counts)
