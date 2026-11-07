# Physical Model: Single-Photon Double-Slit Interference

## 1. Objective

This document establishes the physical and mathematical framework for a computational simulation of single-photon interference in a double-slit experiment.

The main objective is to investigate the statistical emergence of an interference pattern through individual photon detection events and to study the corresponding probability distribution and photon counting statistics.

The model is formulated using quantum probability amplitudes, the Born rule, and scalar wave optics under the paraxial and Fraunhofer approximations.

## 2. Physical Configuration

The system consists of a monochromatic single-photon source, a double-slit aperture, and a position-sensitive detection screen located at a distance \(L\) from the aperture.

The geometrical parameters are defined as:

- \(a\): width of each slit.
- \(d\): center-to-center separation between the slits.
- \(\lambda\): photon wavelength.
- \(L\): propagation distance.
- \(x\): transverse coordinate on the detection screen.

The slit centers are positioned at

\[
x_1=-\frac{d}{2},
\qquad
x_2=+\frac{d}{2}.
\]

## 3. Physical Assumptions

The baseline model adopts the following assumptions:

1. Photons are emitted independently and detected one at a time.
2. The incident photons are monochromatic and mutually coherent.
3. Both slits are illuminated with equal probability amplitudes.
4. The two slits have identical widths.
5. Photon propagation is described using scalar wave optics.
6. The paraxial approximation is valid.
7. The detection screen is in the Fraunhofer regime.
8. No which-path information is available.
9. Photon detection events are statistically independent.

## 4. Mathematical Formulation

### 4.1 Wave Number and Observation Angle

The wave number is defined as

\[
k=\frac{2\pi}{\lambda}.
\]

For small diffraction angles,

\[
\sin\theta\approx\tan\theta\approx\frac{x}{L}.
\]

The transverse wave-vector component is therefore

\[
k_x\approx\frac{2\pi x}{\lambda L}.
\]

### 4.2 Single-Slit Diffraction Amplitude

For a rectangular slit of width \(a\), the Fraunhofer diffraction amplitude is proportional to

\[
A_{\mathrm{slit}}(x)=
\operatorname{sinc}
\left(
\frac{\pi ax}{\lambda L}
\right).
\]

The normalized sinc function is defined as

\[
\operatorname{sinc}(u)=
\begin{cases}
\dfrac{\sin u}{u}, & u\neq 0,\\[6pt]
1, & u=0.
\end{cases}
\]

### 4.3 Double-Slit Probability Amplitude

The total probability amplitude is the coherent superposition of the contributions from the two slits:

\[
\psi(x)=\psi_1(x)+\psi_2(x).
\]

For two identical slits with equal illumination,

\[
\psi(x)\propto
A_{\mathrm{slit}}(x)
\left[
e^{-i\frac{\pi dx}{\lambda L}}
+
e^{i\frac{\pi dx}{\lambda L}}
\right].
\]

Using Euler's identity,

\[
e^{i\phi}+e^{-i\phi}=2\cos\phi,
\]

the total amplitude becomes

\[
\psi(x)\propto
2A_{\mathrm{slit}}(x)
\cos\left(\frac{\pi dx}{\lambda L}\right).
\]

### 4.4 Detection Probability Density: Born Rule

According to the Born rule, the probability density of detecting a photon at position \(x\) is proportional to the squared modulus of its probability amplitude:

\[
P(x)\propto|\psi(x)|^2.
\]

The corresponding unnormalized intensity distribution is

\[
I(x)=I_0
\operatorname{sinc}^2
\left(\frac{\pi ax}{\lambda L}\right)
\cos^2
\left(\frac{\pi dx}{\lambda L}\right).
\]

The normalized probability density over the finite detection interval is

\[
p(x)=
\frac{I(x)}
{\displaystyle\int_{-X_{\max}}^{X_{\max}}I(x')\,dx'}.
\]

The normalization condition is

\[
\int_{-X_{\max}}^{X_{\max}}p(x)\,dx=1.
\]

This probability density determines the statistical distribution of individual photon detection positions.

## 5. Individual Photon Detection

Each photon produces a localized detection event at a transverse position \(x_n\).

The detection position is sampled according to the probability density:

\[
x_n\sim p(x).
\]

For a total of \(N\) detected photons, the accumulated detection distribution is represented by

\[
H_N(x)=\sum_{n=1}^{N}\delta(x-x_n).
\]

Here, \(\delta(x-x_n)\) denotes the Dirac delta distribution.

As the number of detected photons increases, the empirical distribution approaches the theoretical probability density:

\[
\frac{H_N(x)}{N}\longrightarrow p(x).
\]

This convergence is interpreted through finite spatial-bin estimates.

The simulation therefore demonstrates how an interference pattern emerges from the accumulation of individual photon detection events.

## 6. Time Evolution of the Detection Pattern

In the baseline model, time evolution refers to the sequential accumulation of photon detection events.

Let \(N(t)\) denote the number of detected photons up to time \(t\).

The accumulated detection distribution is

\[
H(x,t)=
\sum_{n=1}^{N(t)}\delta(x-x_n).
\]

The normalized empirical distribution is

\[
p_{\mathrm{emp}}(x,t)=
\frac{H(x,t)}{N(t)},
\qquad N(t)>0.
\]

The simulation will visualize the development of the detection pattern at successive detection intervals.

**Note:** This represents the accumulation of detection events rather than a time-dependent solution of the Schrödinger equation.

## 7. Photon Counting Statistics

The detection screen is divided into \(M\) spatial bins.

The probability of detecting a photon in bin \(i\) is

\[
p_i=
\int_{x_i}^{x_{i+1}}p(x)\,dx.
\]

### 7.1 Multinomial Distribution: Fixed Total Photon Number

For a fixed total number \(N\) of detected photons, the joint probability distribution of the bin counts is

\[
P(n_1,\ldots,n_M)=
\frac{N!}{n_1!\cdots n_M!}
\prod_{i=1}^{M}p_i^{n_i}.
\]

The total photon count satisfies

\[
\sum_{i=1}^{M}n_i=N.
\]

The expected number of photons in bin \(i\) is

\[
\mathbb{
