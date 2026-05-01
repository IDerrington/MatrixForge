# Digital Signal Processing

Matrices are fundamental to digital signal processing (DSP). They allow us to efficiently filter, transform, and analyze audio, images, and sensor data.

## What is DSP?

Digital Signal Processing is about manipulating digital representations of signals—sequences of numbers that represent sound waves, images, sensor readings, or any time-varying data.

Common DSP tasks:
- Filtering noise from audio or sensor data
- Detecting patterns or features
- Compressing data
- Transforming between time and frequency domains

## Signals as Vectors

A digital signal is just a sequence of numbers, which we can represent as a vector:

$$
\mathbf{x} = \begin{bmatrix}
x_0 \\
x_1 \\
x_2 \\
\vdots \\
x_{N-1}
\end{bmatrix}
$$

For audio, each $x_i$ might be an amplitude sample at time $i$. For an image, it might represent pixel brightness.

## Filtering with Matrices

Many filters can be expressed as matrix operations. A **convolution filter** applies a weighted sum of neighboring samples.

```python
import numpy as np
import matplotlib.pyplot as plt

# Create a noisy signal
np.random.seed(42)
t = np.linspace(0, 1, 100)
clean_signal = np.sin(2 * np.pi * 5 * t)
noisy_signal = clean_signal + 0.3 * np.random.randn(100)

# Simple moving average filter (smoothing)
window_size = 5
filtered_signal = np.convolve(noisy_signal, np.ones(window_size)/window_size, mode='same')

# Plot
plt.figure(figsize=(10, 6))
plt.plot(t, clean_signal, 'g-', label='Clean signal', linewidth=2)
plt.plot(t, noisy_signal, 'lightgray', label='Noisy signal')
plt.plot(t, filtered_signal, 'b-', label='Filtered signal', linewidth=2)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Signal Filtering')
plt.legend()
plt.grid(True)
plt.show()
```

## The Discrete Fourier Transform (DFT)

The DFT is a matrix that transforms a time-domain signal into the frequency domain. It's one of the most important tools in DSP.

The DFT matrix $\mathbf{F}$ for $N$ samples has elements:

$$
F_{kn} = e^{-i 2\pi kn / N}
$$

Applying this matrix to a signal vector gives its frequency spectrum:

$$
\mathbf{X} = \mathbf{F} \mathbf{x}
$$

```python
import numpy as np

# Simple 4-point DFT example
N = 4
x = np.array([1, 2, 3, 4])

# Compute DFT using numpy
X = np.fft.fft(x)

print("Time domain signal:", x)
print("Frequency domain:", X)
```

The Fast Fourier Transform (FFT) is an efficient algorithm for computing the DFT—but it's still fundamentally a matrix multiplication.

## Convolution as Matrix Multiplication

Convolution, a core operation in DSP and deep learning, can be expressed as matrix multiplication using a **Toeplitz matrix**.

## Applications

DSP with matrices enables:

- **Audio processing**: Equalizers, reverb, noise cancellation
- **Image processing**: Blurring, sharpening, edge detection
- **Communication systems**: Channel estimation, error correction
- **Radar and sonar**: Target detection and tracking
- **Biomedical signals**: ECG/EEG analysis, medical imaging

## Coming Soon

Future sections will dive deeper into:
- Spectral analysis
- Filter design
- Wavelet transforms
- Adaptive filtering

## Next Steps

Explore {doc}`beamforming` to see how matrices focus signals from antenna arrays, or check out {doc}`graphics` for matrix transformations in 3D.
