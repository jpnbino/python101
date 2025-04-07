import numpy as np
import matplotlib.pyplot as plt

# Sampling frequency
fs = 1000

# Time array
t = np.linspace(0, 1, fs)

# Input signal
x = np.sin(2 * np.pi * 1 * t - 0.7853)
x2 = np.cos(2 * np.pi * 1 * t- 0.7853)
# FFT of the signal
X = np.fft.fft(x)
X2 = np.fft.fft(x2)
freq = np.fft.fftfreq(x.size, d=t[1]-t[0])
# Phase angle of the FFT coefficients
phase = np.angle(X)
phase2 = np.angle(X2)
# Plot the phase angle
plt.subplot(4, 1, 1)
plt.plot(t, x)
plt.title('Sine wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')


plt.subplot(4, 1, 2)
plt.plot(freq, phase*180/np.pi)
plt.title('Phase of the FFT coefficients')
plt.xlabel('Frequency')
plt.ylabel('Phase (degree)')

plt.subplot(4, 1, 3)
plt.plot(t, x2)
plt.title('Cosine wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')


plt.subplot(4, 1, 4)
plt.plot(t, phase2*180/np.pi)
plt.title('Phase of the FFT coefficients')
plt.xlabel('Time (s)')
plt.ylabel('Phase (degree)')
plt.tight_layout()
plt.show()
