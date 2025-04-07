import numpy as np
import matplotlib.pyplot as plt

# Define signal parameters
f = 1   # Signal frequency
fs = 16 # Sampling frequency
N = 16  # Number of samples

# Generate signal
t = np.arange(N)/fs
x = np.sin(2*np.pi*f*t)

# Compute DFT without zero-padding
X = np.fft.fft(x)

# Compute DFT with zero-padding
Xzp = np.fft.fft(x, N*2)

# Plot results
fig, axs = plt.subplots(2, 1, figsize=(6, 6))
axs[0].stem(np.abs(X))
axs[0].set_title('DFT without zero-padding')
axs[1].stem(np.abs(Xzp))
axs[1].set_title('DFT with zero-padding')
plt.tight_layout()
plt.show()
