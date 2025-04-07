import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, freqz

# Cutoff frequency
cutoff_frequency = 600
# Sample rate
sample_rate = 20000
# Filter order
order = 2

# Normalized cutoff frequency
nyquist_frequency = sample_rate/2
normalized_cutoff = cutoff_frequency/nyquist_frequency

# Design the high-pass filter
b, a = butter(order, normalized_cutoff, 'highpass')

# Plot the BODE plot
w, h = freqz(b, a, worN=np.logspace(-2, 2, 10000))
plt.plot((w/np.pi)*nyquist_frequency, 20 * np.log10(np.abs(h)), label="IIR High-Pass filter")
plt.xscale('log')
plt.title('Butterworth filter frequency response')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude [dB]')
plt.margins(0, 0.1)
plt.xlim([0, 10e8])
plt.grid(which='both', axis='both')
plt.axvline(cutoff_frequency, color='green') # cutoff frequency
plt.legend()
plt.show()
