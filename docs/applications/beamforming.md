# Beamforming

Beamforming uses matrices to focus antenna arrays, enhancing signals from desired directions while suppressing interference and noise.

## What is Beamforming?

Imagine you have multiple microphones or antennas arranged in an array. Each element receives a slightly different version of the same signal due to differences in distance and angle.

Beamforming combines these signals to:
- **Amplify signals from a target direction**
- **Suppress signals from other directions**
- **Null out interference**

It's like having a directional antenna that you can steer electronically without physically moving anything.

## The Basic Concept

For an array of $N$ sensors, each receives a signal:

$$
\mathbf{x}(t) = \begin{bmatrix}
x_1(t) \\
x_2(t) \\
\vdots \\
x_N(t)
\end{bmatrix}
$$

We apply weights $\mathbf{w}$ to each sensor and sum:

$$
y(t) = \mathbf{w}^H \mathbf{x}(t) = w_1^* x_1(t) + w_2^* x_2(t) + \cdots + w_N^* x_N(t)
$$

The superscript $H$ denotes conjugate transpose, and $*$ denotes complex conjugate.

## Steering Vector

For a signal arriving from direction $\theta$, the phase difference between adjacent sensors creates a **steering vector**:

$$
\mathbf{a}(\theta) = \begin{bmatrix}
1 \\
e^{i 2\pi d \sin\theta / \lambda} \\
e^{i 4\pi d \sin\theta / \lambda} \\
\vdots \\
e^{i 2\pi (N-1) d \sin\theta / \lambda}
\end{bmatrix}
$$

where:
- $d$ = spacing between sensors
- $\lambda$ = wavelength
- $\theta$ = angle of arrival

## Delay-and-Sum Beamforming

The simplest beamformer sets weights to the conjugate of the steering vector:

$$
\mathbf{w} = \frac{\mathbf{a}(\theta_0)}{N}
$$

This aligns signals from direction $\theta_0$ and adds them constructively.

```python
import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 8  # Number of elements
d = 0.5  # Spacing (in wavelengths)
theta_target = 30  # Target angle (degrees)

# Create steering vector
theta_rad = np.deg2rad(theta_target)
k = 2 * np.pi / 1  # Wavenumber (wavelength = 1)
n = np.arange(N)
steering_vector = np.exp(1j * k * d * n * np.sin(theta_rad))

# Weights for delay-and-sum
w = steering_vector.conj() / N

# Compute array response for all angles
angles = np.linspace(-90, 90, 181)
response = []

for angle in angles:
    theta = np.deg2rad(angle)
    a = np.exp(1j * k * d * n * np.sin(theta))
    response.append(np.abs(w.conj() @ a))

response = np.array(response)

# Plot beam pattern
plt.figure(figsize=(10, 6))
plt.plot(angles, 20 * np.log10(response / np.max(response)))
plt.xlabel('Angle (degrees)')
plt.ylabel('Response (dB)')
plt.title(f'Beam Pattern (steering to {theta_target}°)')
plt.grid(True)
plt.axvline(theta_target, color='r', linestyle='--', label='Target direction')
plt.legend()
plt.ylim([-40, 5])
plt.show()
```

## Adaptive Beamforming

Adaptive beamformers use **covariance matrices** to optimize weights based on the received data.

The received signal covariance matrix is:

$$
\mathbf{R} = E[\mathbf{x}(t) \mathbf{x}^H(t)]
$$

Methods like **Minimum Variance Distortionless Response (MVDR)** compute optimal weights:

$$
\mathbf{w}_{\text{MVDR}} = \frac{\mathbf{R}^{-1} \mathbf{a}(\theta_0)}{\mathbf{a}^H(\theta_0) \mathbf{R}^{-1} \mathbf{a}(\theta_0)}
$$

This minimizes output power (noise and interference) while maintaining unit gain toward the target.

## Applications

Beamforming is used in:

- **Wireless communications**: 5G, WiFi, satellite links
- **Radar**: Target detection and tracking
- **Sonar**: Underwater acoustics
- **Medical imaging**: Ultrasound beamforming
- **Astronomy**: Radio telescope arrays
- **Audio**: Microphone arrays for speech enhancement

## Matrix Operations in Beamforming

Key matrix operations:
- **Covariance estimation**: $\mathbf{R} = \frac{1}{M} \sum_{i=1}^{M} \mathbf{x}_i \mathbf{x}_i^H$
- **Matrix inversion**: Computing $\mathbf{R}^{-1}$
- **Eigenvalue decomposition**: MUSIC and ESPRIT algorithms
- **Steering vector computation**: Phase delays as complex exponentials

## Coming Soon

Future sections will explore:
- MUSIC and ESPRIT direction-finding algorithms
- Covariance matrix structure
- Eigenvalues and eigenvectors in array processing
- Spatial filtering

## Next Steps

Beamforming relies heavily on eigenvalues and eigenvectors (coming soon). For now, explore {doc}`least-squares` to see another application of matrix inversion.
