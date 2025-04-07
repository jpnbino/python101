import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

fs = 100000  # Sample rate
cutoff = 600  # Cutoff frequency

# Transfer function coefficients
b = [940, 0, -940]
a = [505.8, -810.94, 309.15]

# Frequency response
w, h = signal.freqz(b, a, fs=fs)

# Plot the magnitude response
plt.subplot(2, 1, 1)
plt.semilogx(w, 20 * np.log10(abs(h)))
plt.title('Magnitude Response')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Magnitude [dB]')
plt.grid(which='both', axis='both')
plt.axvline(cutoff, color='green')  # Add a vertical line at the cutoff frequency

# Plot the phase response
plt.subplot(2, 1, 2)
plt.semilogx(w, np.angle(h)*180/np.pi)
plt.title('Phase Response')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Phase [radians]')
plt.grid(which='both', axis='both')
plt.axvline(cutoff, color='green')  # Add a vertical line at the cutoff frequency

plt.tight_layout()
plt.show()
