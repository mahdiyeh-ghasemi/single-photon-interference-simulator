
import numpy as np
import matplotlib.pyplot as plt


def calculate_probability_density(x):
    """Calculate the normalized double-slit probability density."""

    wavelength = 500e-9
    screen_distance = 1.0
    slit_width = 50e-6
    slit_separation = 200e-6

    u = np.pi * slit_width * x / (wavelength * screen_distance)
    single_slit = np.sinc(u / np.pi)

    phase = (
        np.pi * slit_separation * x
        / (wavelength * screen_distance)
    )

    amplitude = 2.0 * single_slit * np.cos(phase)
    intensity = np.abs(amplitude) ** 2

    normalization = np.sum(intensity)

    return intensity / normalization


def main():

    rng = np.random.default_rng(42)

    # Detector configuration
    number_of_bins = 100
    total_photons = 10000
    number_of_trials = 500

    # Define spatial bins
    bin_edges = np.linspace(-0.01, 0.01, number_of_bins + 1)
    x = 0.5 * (bin_edges[:-1] + bin_edges[1:])
    bin_widths = np.diff(bin_edges)

    # Calculate probability density at bin centers
    probability_density = calculate_probability_density(x)

    # Normalize bin probabilities
    bin_probabilities = probability_density * bin_widths
    bin_probabilities /= np.sum(bin_probabilities)

    # Expected counts
    expected_counts = total_photons * bin_probabilities

    # Multinomial model: fixed total number of photons
    multinomial_sample = rng.multinomial(
        total_photons,
        bin_probabilities
    )

    # Poisson model: independent photon counts
    poisson_sample = rng.poisson(expected_counts)

    # Repeat experiments
    multinomial_trials = np.array([
        rng.multinomial(total_photons, bin_probabilities)
        for _ in range(number_of_trials)
    ])

    poisson_trials = np.array([
        rng.poisson(expected_counts)
        for _ in range(number_of_trials)
    ])

    # Empirical variances
    multinomial_variance = np.var(multinomial_trials, axis=0)
    poisson_variance = np.var(poisson_trials, axis=0)

    # Theoretical variances
    theoretical_multinomial_variance = (
        total_photons
        * bin_probabilities
        * (1 - bin_probabilities)
    )

    theoretical_poisson_variance = expected_counts

    # Create figure
    fig, axes = plt.subplots(2, 2, figsize=(13, 9))

    # Multinomial count distribution
    axes[0, 0].bar(
        x,
        multinomial_sample,
        width=0.00018,
        alpha=0.65,
        label="Simulated counts"
    )
    axes[0, 0].plot(
        x,
        expected_counts,
        color="black",
        linewidth=1.5,
        label="Expected counts"
    )
    axes[0, 0].set_title("Multinomial Photon Counting")
    axes[0, 0].set_xlabel("Screen position (m)")
    axes[0, 0].set_ylabel("Photon counts")
    axes[0, 0].legend()

    # Poisson count distribution
    axes[0, 1].bar(
        x,
        poisson_sample,
        width=0.00018,
        alpha=0.65,
        label="Simulated counts"
    )
    axes[0, 1].plot(
        x,
        expected_counts,
        color="black",
        linewidth=1.5,
        label="Expected counts"
    )
    axes[0, 1].set_title("Poisson Photon Counting")
    axes[0, 1].set_xlabel("Screen position (m)")
    axes[0, 1].set_ylabel("Photon counts")
    axes[0, 1].legend()

    # Multinomial variance comparison
    axes[1, 0].scatter(
        theoretical_multinomial_variance,
        multinomial_variance,
        alpha=0.7
    )

    maximum = max(
        np.max(theoretical_multinomial_variance),
        np.max(multinomial_variance)
    )

    axes[1, 0].plot(
        [0, maximum],
        [0, maximum],
        "k--",
        label="Ideal agreement"
    )
    axes[1, 0].set_title("Multinomial Variance")
    axes[1, 0].set_xlabel("Theoretical variance")
    axes[1, 0].set_ylabel("Empirical variance")
    axes[1, 0].legend()

    # Poisson variance comparison
    axes[1, 1].scatter(
        theoretical_poisson_variance,
        poisson_variance,
        alpha=0.7
    )

    maximum = max(
        np.max(theoretical_poisson_variance),
        np.max(poisson_variance)
    )

    axes[1, 1].plot(
        [0, maximum],
        [0, maximum],
        "k--",
        label="Ideal agreement"
    )
    axes[1, 1].set_title("Poisson Variance")
    axes[1, 1].set_xlabel("Theoretical variance")
    axes[1, 1].set_ylabel("Empirical variance")
    axes[1, 1].legend()

    plt.tight_layout()

    # Save figure
    plt.savefig(
        "figures/photon_counting_statistics.png",
        dpi=300,
        bbox_inches="tight"
    )

    print("Photon counting statistics simulation completed.")
    print(f"Multinomial total: {np.sum(multinomial_sample)}")
    print(f"Poisson total: {np.sum(poisson_sample)}")
    print("Figure saved: photon_counting_statistics.png")

    plt.show()


if __name__ == "__main__":
    main()
