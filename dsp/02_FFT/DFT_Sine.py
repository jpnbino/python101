import numpy as np
import matplotlib.pyplot as plt

# Sampling rate and time step
Fs = 10000 # Hz
T = 1 / Fs # sec

# Define the input signal
A = 1 # Amplitude
w = 6314.6012 # rad/sec
b = 0.7853
n = np.arange(0, 1000)
x = A * np.sin(w * n * T + b)

# Zero padding
x = np.pad(x, (0, 2000), mode='constant')

# DFT
N = len(x)
X = np.zeros(N, dtype=np.complex_)
for k in range(N):
    for n in range(N):
        X[k] += x[n] * np.exp(-1j * 2 * np.pi * k * n / N)

# Plot the magnitude of the DFT
plt.plot(np.abs(X))
plt.xlabel('k')
plt.ylabel('|X(k)|')
plt.show()
