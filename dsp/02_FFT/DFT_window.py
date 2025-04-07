import numpy as np
import matplotlib.pyplot as plt

# Create two signals with frequencies of 10 Hz and 20 Hz
N = 1024
f1 = 11.5
f2 = 15.2
t = np.linspace(0, 2*np.pi, N)
x = np.sin(f1*t) + 0.1*np.sin(f2*t)

# Perform DFT with rectangular window
X_rect = np.abs(np.fft.fft(x))
f_rect = np.fft.fftfreq(N, 1/N)

# Perform DFT with Hann window
w = np.hanning(N)
X_hann = np.abs(np.fft.fft(x * w))
f_hann = np.fft.fftfreq(N, 1/N)

# Plot the results
plt.figure(figsize=(8, 4))
plt.subplot(121)
plt.plot(f_rect, X_rect)
plt.title('Rectangular Window')
plt.xlim(0, 30)
plt.ylim(0, np.max(X_rect))

plt.subplot(122)
plt.plot(f_hann, X_hann)
plt.title('Hann Window')
plt.xlim(0, 30)
plt.ylim(0, np.max(X_hann))

plt.tight_layout()
plt.show()
