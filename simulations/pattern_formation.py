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
    Calculate the normalized double-slit photon detection
    probability density using the Fraunhofer approximation.
    """

    x = np.asarray(x, dtype=float)

    if x.ndim != 1 or len(x) < 2:
        raise ValueError("At least two screen positions are required.")

    if not np.all(np.isfinite(x)):
        raise ValueError("Screen positions must be finite.")

    if np.any(np.diff(x) <= 0):
        raise ValueError("Screen positions must be strictly increasing.")

    if wavelength <= 0 or screen_distance <= 0:
        raise ValueError("Wavelength and screen distance must be positive.")

    if slit_width <= 0 or slit_separation <= 0:
        raise ValueError("Slit dimensions must be positive.")

    # Single-slit diffraction envelope
    u = (
        np.pi * slit_width * x
        / (wavelength * screen_distance)
    )

    single_slit = np.sinc(u / np.pi)

    # Double-slit interference phase
    phase = (
        np.pi * slit_separation * x
        / (wavelength * screen_distance)
    )

    # Coherent double-slit amplitude
    amplitude = 2.0 * single_slit * np.cos(phase)

    # Intensity distribution
    intensity = np.abs(amplitude) ** 2

    # Numerical normalization (compatible with older NumPy)
    normalization = np.trapezoid(intensity, x)
    if not np.isfinite(normalization) or normalization <= 0:
        raise ValueError("Invalid intensity normalization.")

    return intensity / normalization


def sample_photon_positions(
    x,
    probability_density,
    n_photons,
    rng
):
    """
    Generate individual photon detection positions
    using inverse transform sampling.
    """

    x = np.asarray(x, dtype=float)
    probability_density = np.asarray(
        probability_density,
        dtype=float
    )

    if x.ndim != 1 or probability_density.ndim != 1:
        raise ValueError("Input arrays must be one-dimensional.")

    if len(x) != len(probability_density) or len(x) < 2:
        raise ValueError("Input arrays must have equal lengths.")

    if not np.all(np.isfinite(x)) or not np.all(
        np.isfinite(probability_density)
    ):
        raise ValueError("Input arrays must contain finite values.")

    if np.any(np.diff(x) <= 0):
        raise ValueError("Position grid must be strictly increasing.")

    if np.any(probability_density < 0):
        raise ValueError("Probability density cannot be negative.")

    if not isinstance(n_photons, (int, np.integer)) or n_photons < 0:
        raise ValueError("Photon number must be a non-negative integer.")

    if rng is None:
        rng = np.random.default_rng()

    # Probability mass between adjacent grid points
    segment_probability = (
        0.5
        * (
            probability_density[:-1]
            + probability_density[1:]
        )
        * np.diff(x)
    )

    # Cumulative distribution
    cumulative_probability = np.concatenate(
        ([0.0], np.cumsum(segment_probability))
    )

    total_probability = cumulative_probability[-1]

    if not np.isfinite(total_probability) or total_probability <= 0:
        raise ValueError("Total probability must be positive.")

    cumulative_probability /= total_probability

    # Random photon detection positions
    random_values = rng.random(n_photons)

    detections = np.interp(
        random_values,
        cumulative_probability,
        x
    )

    return detections


def main():

    # 1. Physical parameters
    wavelength = 500e-9
    screen_distance = 1.0
    slit_width = 50e-6
    slit_separation = 200e-6

    # 2. Observation screen
    x = np.linspace(-0.015, 0.015, 4000)

    # 3. Calculate theoretical probability density
    probability = calculate_probability_density(
        x,
        wavelength,
        screen_distance,
        slit_width,
        slit_separation
    )

    # 4. Simulate individual photon detections
    n_photons = 10000

    rng = np.random.default_rng(seed=42)

    detections = sample_photon_positions(
        x,
        probability,
        n_photons,
        rng
    )

    # 5. Plot theoretical probability density
    plt.figure(figsize=(10, 5))

    plt.plot(
        x * 1e3,
        probability * 1e-3,
        linewidth=2,
        label="Theoretical probability density"
    )

    # 6. Plot accumulated photon detections
    plt.hist(
        detections * 1e3,
        bins=150,
        density=True,
        alpha=0.6,
        label="Simulated photon detections"
    )

    plt.xlabel("Screen position (mm)")
    plt.ylabel("Probability density (1/mm)")

    plt.title(
        "Formation of a Double-Slit Interference Pattern "
        "from Individual Photon Detections"
    )

    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()

    # 7. Save the figure
    output_directory = "figures"

    import os
    os.makedirs(output_directory, exist_ok=True)

    figure_path = os.path.join(
        output_directory,
        "single_photon_pattern.png"
    )

    plt.savefig(
        figure_path,
        dpi=300,
        bbox_inches="tight"
    )

    print("Simulation completed successfully.")
    print(f"Number of photons: {n_photons}")
    print(f"Figure saved to: {figure_path}")

    plt.show()


if __name__ == "__main__":
    main()
