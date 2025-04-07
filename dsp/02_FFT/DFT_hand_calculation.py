import numpy as np
import matplotlib.pyplot as plt

# Define signal parameters
fs = 100  # sampling frequency
T = 1/fs  # sampling period
t = np.arange(0, 1, T)  # time axis
f = 1  # signal frequency
A = 1  # signal amplitude

# Generate signal
#x = A * np.sin(2 * np.pi * f * t)

# Define input sequence
x = np.array([0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1,])

# Define the DFT size
N = len(x)

# Initialize the DFT output array
X = np.zeros(N, dtype=np.complex_)

# Perform the DFT
for k in range(N):
    for n in range(N):
        X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)

# Print the result
print(X)

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