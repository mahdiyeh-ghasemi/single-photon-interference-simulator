# Theoretical Background: Single-Photon Interference

## 1. Introduction

The double-slit experiment is a fundamental demonstration of the wave-particle duality of quantum objects.

In classical wave optics, interference results from the superposition of coherent waves. In quantum mechanics, however, the same interference phenomenon can be observed even when photons are emitted and detected individually.

Each photon produces a localized detection event. Nevertheless, after many independent detections, an interference distribution gradually emerges.

This behavior demonstrates that quantum interference is governed by probability amplitudes rather than by the classical trajectory of an individual photon.

## 2. Wave-Particle Duality

Wave-particle duality describes the complementary wave-like and particle-like properties of quantum systems.

In the double-slit experiment, the wave-like behavior is associated with the interference of probability amplitudes, whereas the particle-like behavior is observed through localized photon detection events.

The two descriptions are not contradictory. They represent different aspects of the same quantum phenomenon.

The interference pattern is a statistical result of many individual detection events.

## 3. Quantum Superposition

Quantum superposition is a fundamental principle stating that a quantum system can be described by a linear combination of possible states.

In the double-slit experiment, when no which-path information is available, the photon probability amplitude at the detection screen is the coherent sum of the amplitudes associated with the two slits.

The total amplitude is therefore expressed as:

`ψ(x)=ψ₁(x)+ψ₂(x)`

The corresponding detection probability is proportional to the squared modulus of the total amplitude:

`P(x)=|ψ₁(x)+ψ₂(x)|²`

Expanding this expression gives:

`P(x)=|ψ₁(x)|²+|ψ₂(x)|²+2Re[ψ₁*(x)ψ₂(x)]`

The last term represents the interference contribution.

This term distinguishes coherent quantum superposition from the addition of independent classical intensities.

## 4. The Born Rule

The Born rule establishes the relationship between a quantum probability amplitude and the probability density of a measurement outcome.

For a photon detected at position $x$, the probability density is proportional to the squared modulus of its wavefunction:

$$
p(x)\propto |\psi(x)|^2
$$

For a normalized probability density over a finite detection-screen interval, the expression becomes:

$$
p(x)=\frac{|\psi(x)|^2}{\displaystyle\int_{x_{\min}}^{x_{\max}}|\psi(x)|^2\,dx}
$$

The normalization condition is:

$$
\int_{x_{\min}}^{x_{\max}}p(x)\,dx=1
$$

The Born rule provides the theoretical foundation for generating photon detection positions in the numerical simulation.

Each simulated photon is assigned one detection position according to this probability distribution.

## 5. Single-Photon Interference

Single-photon interference demonstrates that an interference pattern does not require multiple photons to be present simultaneously.

When photons are emitted individually, each photon produces one localized detection event.

The detection positions are distributed probabilistically. As the number of detected photons increases, the spatial distribution gradually reveals the interference pattern.

The essential distinction is between an individual detection event and the statistical distribution of many events.

A single photon does not produce a complete interference pattern on the detection screen. The pattern emerges through repeated measurements.

## 6. Which-Path Information and Interference

The existence of interference depends on the coherence between the possible paths.

When no which-path information is available, the probability amplitudes associated with the two slits can interfere.

If the paths become distinguishable through a which-path measurement, the interference contribution is reduced or may disappear.

For two possible paths, the coherent probability distribution contains the cross term:

`2Re[ψ₁*(x)ψ₂(x)]`

If coherence is completely lost, this term vanishes and the probability distribution becomes an incoherent sum:

`P(x)=|ψ₁(x)|²+|ψ₂(x)|²`

The baseline simulation considers the coherent case and does not implement which-path detection.

## 7. Statistical Emergence of the Interference Pattern

The detection position of each photon is a random variable governed by the quantum probability density.

For a sequence of independent detection events, the measured distribution is constructed by accumulating individual photon detection positions.

The probability of detecting a photon within a spatial interval is obtained by integrating the normalized probability density over that interval.

For a spatial bin extending from $x_i$ to $x_{i+1}$, the corresponding detection probability is:

$$
p_i=\int_{x_i}^{x_{i+1}}p(x)\,dx
$$

The probabilities of all spatial bins satisfy:

$$
\sum_{i=1}^{M}p_i=1
$$

After many detection events, the relative frequency of detections in each bin approaches its theoretical probability.

This statistical behavior is consistent with the law of large numbers.

The simulation uses this principle to demonstrate the gradual formation of the interference pattern through sequential photon detection.

## 8. Photon Counting Statistics

Photon counting statistics describe the fluctuations in the number of detected photons across spatial detector bins.

For a fixed total number of detected photons $N$ distributed among $M$ detector bins, the counts follow a multinomial distribution.

The joint probability of observing counts $n_1,n_2,\ldots,n_M$ is:

$$
P(n_1,\ldots,n_M)=
\frac{N!}{n_1!n_2!\cdots n_M!}
\prod_{i=1}^{M}p_i^{n_i}
$$

where:

$$
\sum_{i=1}^{M}n_i=N
$$

The expected count and variance in bin $i$ are:

$$
\mathbb{E}[n_i]=Np_i
$$

$$
\mathrm{Var}(n_i)=Np_i(1-p_i)
$$

In contrast, when photon counts in different detector bins are modeled as independent Poisson random variables, the count in bin $i$ follows:

$$
P(n_i)=\frac{\mu_i^{n_i}e^{-\mu_i}}{n_i!}
$$

where $\mu_i$ is the expected number of photons in that bin.

For a Poisson distribution, the mean and variance are equal:

$$
\mathbb{E}[n_i]=\mathrm{Var}(n_i)=\mu_i
$$

These two statistical models describe different counting conditions:

- **Multinomial statistics:** The total number of detected photons is fixed, so counts across bins are statistically dependent.
- **Poisson statistics:** Counts in different bins are independent, and the total number of detected photons can fluctuate.

The simulation compares the empirical counting variances with their theoretical predictions over repeated experiments.

## 9. Connection Between Theory and Numerical Simulation

The theoretical concepts described in this document are implemented through three complementary numerical simulations.

**Simulation 1: Single-Photon Interference Pattern**

1. Calculate the theoretical double-slit probability density.
2. Normalize the probability density over the detection-screen interval.
3. Generate individual photon detection positions using random sampling.
4. Construct a spatial histogram of the accumulated detection events.
5. Compare the simulated distribution with the theoretical probability density.

**Simulation 2: Sequential Photon Detection**

1. Generate a sequence of individual photon detection events.
2. Accumulate the detection positions sequentially.
3. Construct cumulative histograms at selected detection counts.
4. Examine how the interference pattern becomes clearer as the number of detected photons increases.

**Simulation 3: Photon Counting Statistics**

1. Divide the detection-screen interval into spatial bins.
2. Calculate the probability associated with each bin.
3. Generate photon counts using multinomial and Poisson statistical models.
4. Repeat the simulations to estimate empirical counting variances.
5. Compare the empirical variances with their theoretical predictions.

Together, these simulations connect quantum probability amplitudes, individual photon detection events, and statistical counting behavior.

The numerical results illustrate how the theoretical probability distribution is reflected in the accumulated measurement statistics.

## 10. Conclusion

Single-photon double-slit interference provides an important demonstration of the probabilistic nature of quantum mechanics.

The phenomenon connects fundamental concepts including quantum superposition, the Born rule, coherence, and statistical measurement.

The numerical simulations developed in this project investigate three aspects of single-photon interference: the formation of the interference pattern, its gradual emergence through sequential photon detection, and the statistical properties of photon counting.

The results illustrate how individual localized detection events collectively reproduce the probability distribution predicted by quantum theory.

This theoretical background establishes the foundation for the physical model and computational methods implemented in the accompanying project.
