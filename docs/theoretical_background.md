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

The Born rule establishes the relationship between a quantum probability amplitude and the probability of obtaining a measurement outcome.

For a photon detected at position `x`, the probability density is proportional to:

`P(x)=|ψ(x)|²`

For a normalized probability distribution:

`∫P(x)dx=1`

The Born rule provides the theoretical foundation for generating photon detection positions in the numerical simulation.

Each simulated photon is assigned one detection position according to the probability distribution.

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

The detection position of each photon is a random variable governed by the quantum probability distribution.

For a sequence of independent detections, the measured distribution is constructed by accumulating the individual detection positions.

The probability of detecting a photon within a spatial interval is obtained by integrating the probability density over that interval.

For a spatial bin extending from `xᵢ` to `xᵢ₊₁`:

`pᵢ=∫[xᵢ,xᵢ₊₁]p(x)dx`

After many detection events, the relative frequency of detections in each bin approaches its theoretical probability.

This statistical behavior is consistent with the law of large numbers.

The simulation uses this principle to demonstrate the gradual formation of the interference pattern.

## 8. Photon Counting
