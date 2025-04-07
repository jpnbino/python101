import numpy as np
import matplotlib.pyplot as plt

# Sampling rate and time array
fs = 1000
T = 1/fs
t = np.arange(0,1,T)

# Sine wave with frequency of 100Hz
x = np.sin(2*np.pi*100*t + 0.7853)

# Perform FFT
X = np.fft.fft(x)

# Plot magnitude and phase of FFT
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10,8))
ax1.plot(np.abs(X))
ax1.set_xlabel('Frequency Bin')
ax1.set_ylabel('Magnitude')
ax2.plot(np.angle(X)*180/np.pi)
ax2.set_xlabel('Frequency Bin')
ax2.set_ylabel('Phase [radians]')
plt.tight_layout()
plt.show()