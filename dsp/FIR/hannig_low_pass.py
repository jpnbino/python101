import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz, convolve


def hanning_window(filter_length, cut_off_frequency, sample_rate):
    n = np.arange(filter_length)
    w = 0.5 - 0.5 * np.cos(2 * np.pi * n / (filter_length - 1))
    fc = cut_off_frequency / (sample_rate / 2)
    Hd = 2 * fc * np.sinc(2 * fc * (n - (filter_length - 1) / 2))
    Hd = Hd * w
    return Hd

filter_length = 53
cut_off_frequency = 500
sample_rate = 10e3
taps = hanning_window(filter_length, cut_off_frequency, sample_rate)
print(taps)


# Calculate impulse response
impulse = np.zeros(16)
impulse[0] = 1
h = np.real(convolve(taps, impulse))

# Plot impulse response
plt.figure()
plt.stem(h)
plt.title('Impulse response')
plt.xlabel('Sample number')
plt.ylabel('Amplitude')

# Calculate magnitude response
w, H = freqz(taps,fs= 10e3)

# Plot magnitude response
plt.figure()
plt.plot(w, 20 * np.log10(np.abs(H)))
plt.title('Magnitude response')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude [dB]')
plt.grid()

plt.show()