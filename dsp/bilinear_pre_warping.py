import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Sample rate and cutoff frequencies
fs = 15e3
low = 500
high = 1000

# Pre-warping
wp = 2 * fs * np.tan(np.pi * np.array([low, high]) / fs) / np.pi

# Transfer function coefficients
b, a = signal.butter(5, wp, btype='bandpass', analog=True)

# Bilinear transform
b, a = signal.bilinear(b, a, fs)

# Frequency response
w, h = signal.freqz(b, a)

# Plot the frequency response
plt.plot(w / np.pi * fs / 2, 20 * np.log10(np.abs(h)))
plt.xscale('log')
plt.title('Frequency response')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude (dB)')
plt.grid(True)
plt.axis([10, fs / 2, -60, 3])
plt.show()


