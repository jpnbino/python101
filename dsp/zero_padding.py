import numpy as np
import matplotlib.pyplot as plt

# Generate a discrete signal with 10 samples
N = 10
t = np.linspace(0, 1, N)
f = np.sin(2 * np.pi * 10 * t)

# Zero pad the signal to length 20
M = 1024
f_pad = np.pad(f, (0, M - N), mode='constant')

# Compute the FFT of the original and padded signals
F = np.fft.fft(f)
F_pad = np.fft.fft(f_pad)

# Compute the frequency axis for the FFT results
freq = np.fft.fftfreq(N, d=1/N)
freq_pad = np.fft.fftfreq(M, d=1/M)

# Plot the original and padded signals and their FFT results
plt.figure()
plt.subplot(3, 1, 1)
plt.plot(t, f)
plt.title('Original Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 2)
plt.plot(np.linspace(0, 1, M), f_pad)
plt.title('Zero Padded Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 3)
plt.plot(freq, np.abs(F), 'o-', label='Original')
plt.plot(freq_pad, np.abs(F_pad), 'x-', label='Zero Padded')
plt.title('FFT Results')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.legend()

plt.tight_layout()
plt.show()
