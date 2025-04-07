import numpy as np
import matplotlib.pyplot as plt

# Generate a noisy signal with a main frequency of 60Hz
fs = 1000  # Sample rate (samples/second)
T = 1/fs  # Sample interval
N = 1000  # Number of samples
t = np.linspace(0, (N-1)*T, N)  # Time vector
f0 = 60  # Main frequency (Hz)
noise = np.random.normal(0, 1, N)  # Generate random noise
x = np.sin(2*np.pi*f0*t) + noise  # Add noise to the sine wave

# Plot the noisy signal in the time domain

plt.figure(figsize=(10,5))
plt.subplot(2, 1, 1)
plt.plot(t, x, label='Noisy signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Noisy signal in the time domain')
plt.grid()
plt.legend()


# Compute the Fourier Transform of the noisy signal
xf = np.fft.fft(x)
xf = np.fft.fftshift(xf)
f = np.fft.fftfreq(N, T)
f = np.fft.fftshift(f)

# Plot the frequency spectrum of the noisy signal
plt.subplot(2, 1, 2)
plt.plot(f, np.abs(xf), label='Noisy signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Frequency spectrum of the noisy signal')
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()
