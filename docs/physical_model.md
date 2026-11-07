# Physical Model: Single-Photon Double-Slit Interference

## 1. Objective

This document defines the theoretical and mathematical framework for simulating single-photon interference in a double-slit experiment.

The simulation describes how individual photon detection events, accumulated sequentially on a detection screen, produce an interference distribution consistent with the quantum-mechanical probability density.

The model focuses on three aspects:

1. Spatial interference distribution.
2. Sequential accumulation of photon detection events.
3. Statistical properties of photon counts.

The present model assumes coherent illumination and does not include a which-path measurement.

## 2. Physical Configuration

Consider a monochromatic photon with wavelength $\lambda$ incident on two identical parallel slits.

The relevant parameters are:

- $a$: width of each slit.
- $d$: center-to-center distance between the slits.
- $L$: distance between the double slit and the detection screen.
- $\lambda$: photon wavelength.
- $x$: transverse coordinate on the detection screen.

The slit centers are located at

$$
x_1=-\frac{d}{2},
\qquad
x_2=+\frac{d}{2}.
$$

We assume the Fraunhofer diffraction regime:

$$
L\gg \frac{a^2}{\lambda},
\qquad
L\gg \frac{d^2}{\lambda}.
$$

Under this approximation, the transverse wave-vector component is

$$
k_x \simeq \frac{2\pi x}{\lambda L}.
$$

## 3. Single-Slit Diffraction Amplitude

For a uniformly illuminated slit of width $a$, the far-field amplitude is proportional to the sinc function:

$$
A_{\mathrm{slit}}(x)
=
\operatorname{sinc}
\left(
\frac{\pi ax}{\lambda L}
\right).
$$

Here, the normalized sinc function is defined as

$$
\operatorname{sinc}(u)
=
\begin{cases}
\frac{\sin u}{u}, & u\neq 0,\\
1, & u=0.
\end{cases}
$$

This term describes the diffraction envelope associated with the finite slit width.

## 4. Double-Slit Wavefunction

The total probability amplitude is obtained by coherently adding the contributions from the two slits.

The relative phase difference between the two paths is

$$
\Delta\phi(x)
=
\frac{2\pi dx}{\lambda L}.
$$

Therefore, the total amplitude can be written as

$$
\psi(x)
\propto
A_{\mathrm{slit}}(x)
\left[
e^{-i\pi dx/(\lambda L)}
+
e^{i\pi dx/(\lambda L)}
\right].
$$

Using the identity

$$
e^{-i\theta}+e^{i\theta}=2\cos\theta,
$$

we obtain

$$
\psi(x)
\propto
2A_{\mathrm{slit}}(x)
\cos\left(\frac{\pi dx}{\lambda L}\right).
$$

## 5. Quantum Probability Density

According to the Born rule, the probability density of detecting a photon at position $x$ is proportional to the squared modulus of the wavefunction:

$$
P(x)\propto |\psi(x)|^2.
$$

Consequently, the unnormalized interference intensity is

$$
I(x)
=
I_0
\operatorname{sinc}^2
\left(
\frac{\pi ax}{\lambda L}
\right)
\cos^2
\left(
\frac{\pi dx}{\lambda L}
\right),
$$

where $I_0$ is an overall intensity scale.

The first factor determines the diffraction envelope, while the second factor describes the interference fringes.

For a finite detection-screen interval $[-X_{\max},X_{\max}]$, the normalized probability density is

$$
p(x)
=
\frac{I(x)}
{\displaystyle
\int_{-X_{\max}}^{X_{\max}} I(u)\,du
}.
$$

Thus,

$$
\int_{-X_{\max}}^{X_{\max}}p(x)\,dx=1.
$$

This normalized distribution is used for generating individual photon detection positions.

## 6. Individual Photon Detection

Each photon is detected at a single position on the screen.

The detection position of the $n$-th photon is modeled as a random variable sampled from the probability density:

$$
x_n\sim p(x).
$$

For a sequence of $N$ independent photon detections, the measured positions are

$$
\{x_1,x_2,\ldots,x_N\}.
$$

Each detection contributes one localized event rather than a fraction of a photon distributed across the screen.

The interference pattern emerges statistically from the accumulation of these individual detection events.

## 7. Sequential Accumulation of Detection Events

The accumulated detection distribution after $N$ photons can be represented by

$$
H_N(x)
=
\sum_{n=1}^{N}\delta(x-x_n),
$$

where $\delta$ denotes the Dirac delta distribution.

For numerical simulations, the screen is divided into discrete spatial bins. The number of detections in each bin is recorded.

As the number of detected photons increases, the normalized empirical distribution approaches the theoretical probability density:

$$
\frac{H_N(x)}{N}
\longrightarrow p(x)
\qquad
\text{as }N\rightarrow\infty,
$$

where the convergence is understood in the statistical sense and, numerically, through appropriately normalized histograms.

## 8. Photon Counting Statistics

### 8.1 Spatial Bin Probabilities

Let the detection screen be divided into $M$ bins.

The probability of detecting a photon in bin $i$ is

$$
p_i
=
\int_{x_i}^{x_{i+1}}p(x)\,dx.
$$

The probabilities satisfy

$$
\sum_{i=1}^{M}p_i=1,
$$

provided that the bins cover the entire modeled screen interval.

### 8.2 Multinomial Distribution

For a fixed total number of $N$ independently detected photons, the probability of observing counts $n_1,\ldots,n_M$ in the corresponding bins is described by the multinomial distribution:

$$
P(n_1,\ldots,n_M)
=
\frac{N!}{n_1!n_2!\cdots n_M!}
\prod_{i=1}^{M}p_i^{n_i},
$$

subject to

$$
\sum_{i=1}^{M}n_i=N.
$$

The expected count in bin $i$ is

$$
\mathbb{E}[n_i]=Np_i.
$$

The corresponding variance is

$$
\operatorname{Var}(n_i)
=
Np_i(1-p_i).
$$

### 8.3 Poisson Counting Statistics

If photon arrivals are modeled as an independent Poisson process, the count in bin $i$ can instead be described by

$$
P(n_i)
=
\frac{\mu_i^{n_i}e^{-\mu_i}}{n_i!},
$$

where $\mu_i$ is the expected number of detections in that bin.

The expected count and variance are both

$$
\mathbb{E}[n_i]
=
\operatorname{Var}(n_i)
=
\mu_i.
$$

The multinomial and Poisson models represent different counting assumptions and are not interchangeable without specifying the photon-arrival model.

## 9. Numerical Validation

The implementation should be tested against the following physical and statistical conditions:

1. **Normalization:** The numerically calculated probability density must integrate to unity over the selected screen interval.

2. **Symmetry:** For identical slits under symmetric illumination, the theoretical distribution must satisfy

$$
p(-x)=p(x).
$$

3. **Interference-fringe spacing:** The approximate distance between adjacent interference maxima is

$$
\Delta x=\frac{\lambda L}{d}.
$$

4. **Diffraction envelope:** The single-slit envelope must be consistent with the finite slit width.

5. **Statistical convergence:** The simulated detection histogram should approach the theoretical probability distribution as the number of detected photons increases.

6. **Counting statistics:** Numerical count fluctuations should be consistent with the selected multinomial or Poisson model.

## 10. Model Assumptions and Limitations

The baseline model uses the following assumptions:

- Monochromatic photon illumination.
- Two identical, parallel slits.
- Coherent contributions from both slits.
- Uniform illumination across each slit.
- Fraunhofer diffraction approximation.
- Independent photon detection events.
- Ideal detection without detector noise or
