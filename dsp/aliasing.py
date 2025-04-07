import numpy as np
import matplotlib.pyplot as plt

# Generate a continuous cosine wave with 100 Hz frequency
f_sig = 100
t_sig = np.linspace(0, 1, 1000)
sig = np.cos(2 * np.pi * f_sig * t_sig)

# Choose a sample frequency that is under the Nyquist frequency
f_sample = 50
t_sample = np.linspace(0, 1, f_sample)
sig_sample = np.cos(2 * np.pi * f_sig * t_sample)

# Plot the original continuous signal and the sampled signal
plt.figure()
plt.plot(t_sig, sig, label='Continuous Signal')
plt.plot(t_sample, sig_sample, 'o', label='Sampled Signal')
plt.title('Aliasing Example')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.show()

# Calculate the FFT of the sampled signal
sig_fft = np.fft.fft(sig_sample)
f_fft = np.fft.fftfreq(sig_fft.size, 1/f_sample)

# Plot the FFT spectrum
plt.figure()
plt.plot(f_fft, np.abs(sig_fft), label='FFT of Sampled Signal')
plt.title('FFT Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.legend()
plt.show()
