# Single-Photon Interference Simulator

A Python-based simulation of single-photon double-slit interference, including interference pattern formation, sequential photon detection, and photon counting statistics.

## Project Overview

This project investigates how individual photon detection events gradually build up an interference pattern in a double-slit experiment.

The simulation uses a wave-based probability distribution to generate individual photon detection positions and studies the statistical emergence of the interference pattern.

## Simulation Results

### Single-Photon Interference Pattern

The following figure shows the accumulated detection pattern generated from 10,000 simulated photons.

![Single-Photon Interference Pattern](figures/single_photon_pattern.png)

### Sequential Photon Detection

This simulation demonstrates how an interference pattern gradually emerges through the sequential detection of individual photons.

A single sequence of 10,000 photon detection events is generated. The cumulative detection distributions are examined after 10, 100, 500, 1,000, 5,000, and 10,000 detections.

The theoretical probability density is plotted alongside each cumulative histogram to illustrate the statistical emergence of the double-slit interference pattern.

![Sequential Photon Detection](figures/sequential_photon_detection.png)

## Technologies

- Python
- NumPy
- SciPy
- Matplotlib
- Jupyter Notebook

## Project Status

The initial single-photon interference pattern simulation has been implemented and executed successfully. Further development will include time evolution and photon counting statistics.
