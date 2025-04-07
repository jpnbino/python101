import numpy as np
import matplotlib.pyplot as plt

# Sample rate
fs = 100

# Number of sample points
N = 1024

# Generate time array
T = 1/fs
t = np.linspace(0, (N-1)*T, N)

# Generate sinewave with 10Hz frequency
f = 10
x = np.cos(2*np.pi*f*t - 0.7853)

# Calculate FFT
X = np.fft.fft(x)

# Get magnitude and phase
magnitude = np.abs(X)
phase = np.angle(X)

# Normalize magnitude and phase
magnitude = magnitude/N
magnitude = magnitude[range(N//2)]
phase = phase[range(N//2)]

# Plot magnitude and phase
f = np.linspace(0, fs/2, N//2)
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(f, magnitude)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")

plt.subplot(1, 2, 2)
plt.plot(f, 360+phase*180/np.pi)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase (Radians)")

plt.show()
