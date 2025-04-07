import numpy as np
import matplotlib.pyplot as plt

# Sampling rate and time vector
fs = 500 # Hz
T = 1/fs
t = np.linspace(0, 1, fs, endpoint=False)

# Generate sine wave
f0 = 100 # Hz
x = np.sin(2 * np.pi * f0 * t)

# Calculate FFT
X = np.fft.fft(x)
magnitude = np.abs(X)
phase = np.angle(X)

# Plot magnitude response
plt.figure()
plt.plot(magnitude)
plt.title('Magnitude Response')

# Plot phase response
plt.figure()
plt.plot(phase)
plt.title('Phase Response')

# Show the plots
plt.show()
