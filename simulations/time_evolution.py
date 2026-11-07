
import numpy as np
import matplotlib.pyplot as plt


def calculate_probability_density(
    x,
    wavelength,
    screen_distance,
    slit_width,
    slit_separation
):
    """
    Calculate the normalized double-slit detection probability density.
    """

    u = (
        np.pi * slit_width * x
        / (wavelength * screen_distance)
    )

    single_slit = np.sinc(u / np.pi)

    phase = (
        np.pi * slit_separation * x
        / (wavelength * screen_distance)
    )

    amplitude = 2.0 * single_slit * np.cos(phase)

    intensity = np.abs(amplitude) ** 2

    # Numerical integration using the trapezoidal rule
    normalization = np.sum(
        0.5 * (intensity[:-1] + intensity[1:]) * np.diff(x)
    )

    if normalization <= 0 or not np.isfinite(normalization):
        raise ValueError("Invalid intensity normalization.")

    return intensity / normalization


def sample_photons(x, probability_density, n_photons, rng):
    """
    Generate individual photon detection positions.
    """

    dx = np.diff(x)

    cumulative_probability = np.zeros_like(x)

    cumulative_probability[1:] = np.cumsum(
        0.5
        * (probability_density[:-1] + probability_density[1:])
        * dx
    )

    cumulative_probability /= cumulative_probability[-1]

    random_values = rng.random(n_photons)

    return np.interp(
        random_values,
        cumulative_probability,
        x
    )


def main():

    # Physical parameters

    wavelength = 500e-9
    screen_distance = 1.0
    slit_width = 50e-6
    slit_separation = 200e-6

    # Screen coordinates

    x = np.linspace(-0.01, 0.01, 2000)

    # Theoretical probability density

    probability = calculate_probability_density(
        x,
        wavelength,
        screen_distance,
        slit_width,
        slit_separation
    )

    # Generate one sequence of photon detections

    total_photons = 10000

    rng = np.random.default_rng(42)

    detections = sample_photons(
        x,
        probability,
        total_photons,
        rng
    )

    # Cumulative photon counts

    photon_numbers = [10, 100, 500, 1000, 5000, 10000]

    bins = np.linspace(x.min(), x.max(), 101)

    # Plot cumulative detection patterns

    fig, axes = plt.subplots(
        2, 3,
        figsize=(15, 8),
        sharex=True,
        sharey=True
    )

    for ax, number in zip(axes.flat, photon_numbers):

        ax.hist(
            detections[:number],
            bins=bins,
            density=True,
            histtype="step",
            linewidth=1.5,
            label="Photon detections"
        )

        ax.plot(
            x,
            probability,
            "r--",
            linewidth=1.5,
            label="Theoretical probability"
        )

        ax.set_title(f"{number:,} photons")
        ax.set_xlabel("Screen position (m)")
        ax.set_ylabel("Probability density")
        ax.legend(fontsize=8)
        ax.grid(alpha=0.3)

    plt.suptitle(
        "Sequential Build-up of Single-Photon Interference",
        fontsize=14
    )

    plt.tight_layout()

    plt.savefig(
        "figures/sequential_photon_detection.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()

    print("Sequential detection simulation completed.")
    print(f"Total photons: {total_photons}")
    print(
        "Figure saved to: "
        "figures/sequential_photon_detection.png"
    )


if __name__ == "__main__":
    main()
