import numpy as np
import matplotlib.pyplot as plt

# Define signal parameters
fs = 100  # sampling frequency
T = 1/fs  # sampling period
t = np.arange(0, 1, T)  # time axis
f = 1  # signal frequency
A = 1  # signal amplitude

# Generate signal
x = A * np.sin(2 * np.pi * f * t)

# Compute FFT without zero-padding
N = len(x)
X = np.fft.fft(x)/N
freq = np.fft.fftfreq(N, T)
mag = np.abs(X)
phase = np.angle(X)

# Compute FFT with zero-padding (Nfft = 1024)
Nfft = 100
Xp = np.fft.fft(x, Nfft)/Nfft
freqp = np.fft.fftfreq(Nfft, T)
magp = np.abs(Xp)
phasep = np.angle(Xp)

# Plot FFT magnitude and phase
fig, ax = plt.subplots(2, 2, figsize=(10, 8))
ax[0, 0].plot(freq, mag)
ax[0, 0].set_title("FFT Magnitude (No zero-padding)")
ax[0, 0].set_xlabel("Frequency (Hz)")
ax[0, 0].set_ylabel("Magnitude")

ax[0, 1].plot(freqp, magp)
ax[0, 1].set_title("FFT Magnitude (Zero-padding)")
ax[0, 1].set_xlabel("Frequency (Hz)")
ax[0, 1].set_ylabel("Magnitude")

ax[1, 0].plot(freq, phase)
ax[1, 0].set_title("FFT Phase (No zero-padding)")
ax[1, 0].set_xlabel("Frequency (Hz)")
ax[1, 0].set_ylabel("Phase (radians)")

ax[1, 1].plot(freqp, phasep)
ax[1, 1].set_title("FFT Phase (Zero-padding)")
ax[1, 1].set_xlabel("Frequency (Hz)")
ax[1, 1].set_ylabel("Phase (radians)")

plt.tight_layout()
plt.show()
