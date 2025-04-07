'''
Creates a noisy signal and using the amplitude thresholding strategy, removes the noise.
'''
import numpy as np
import matplotlib.pyplot as plt

# Generate a noisy signal with a main frequency of 60Hz
fs = 1000 # Sampling frequency
t = np.linspace(0, 1, fs, endpoint=False) # Sampling times

mean = 0
std = 1 
signal = np.sin(2*np.pi*60*t) + 3*np.random.normal(mean, std, size=len(t)) # noisy signal

# Compute the FFT of the signal
fft_signal = np.fft.fft(signal)
fft_signal_noisy = np.fft.fft(signal)
f = np.fft.fftfreq(len(signal), 1/fs)

# Remove all the bins with an amplitude lower than one third of the highest amplitude bin
highest_amplitude = np.abs(fft_signal).max()
fft_signal[np.abs(fft_signal) < highest_amplitude/1.5] = 0

# Reconstruct the signal based on the remaining bins
reconstructed_signal = np.fft.ifft(fft_signal).real

# Plot the results
plt.figure(figsize=(12, 8))
plt.subplot(411)
plt.title("Noisy Signal")
plt.plot(t, signal)
plt.xlabel("Time (s)")

plt.subplot(412)
#plt.title("FFT Noisy Signal")
plt.plot(f, np.abs(fft_signal_noisy))
plt.xlabel("freq ")

plt.subplot(413)
plt.title("Reconstructed Signal")
plt.plot(t, reconstructed_signal)
plt.xlabel("Time (s)")

plt.subplot(414)
#plt.title("FFT reconstructed Signal")
plt.plot(f, np.abs(fft_signal))
plt.xlabel("freq ")

plt.tight_layout()
plt.show()
