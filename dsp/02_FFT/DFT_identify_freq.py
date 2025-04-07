import numpy as np
import matplotlib.pyplot as plt

# Generate a noisy signal with a known frequency
f = 3 # frequency in Hz
fs = 100 # sample rate in Hz
T = 1/fs # sample period
t = np.arange(0, 1, T) # time vector

mean = 0
std = 1 
x = np.sin(2*np.pi*f*t) + 1*np.random.normal(mean, std, size=len(t)) # noisy signal


# Compute the DFT of the noisy signal without zero padding
X = np.fft.fft(x)
f_no_padding = np.fft.fftfreq(len(x), d=T) # frequency vector
X_no_padding = np.abs(X)

# Compute the DFT of the noisy signal with different amounts of zero padding
N_zeros = [32, 64, 128, 512, 1024]
X_zeros = []
f_zeros = []
for N_zero in N_zeros:
    x_zero = np.pad(x, (0, N_zero), 'constant')
    X_zero = np.fft.fft(x_zero)
    f_zero = np.fft.fftfreq(len(x_zero), d=T)
    X_zeros.append(np.abs(X_zero))
    f_zeros.append(f_zero)

# Plot the DFT of the noisy signal with different amounts of zero padding
plt.figure(figsize=(15, 10))
plt.subplot(611)
plt.plot(f_no_padding, X_no_padding)
plt.xlim([0, 10])
plt.title("No zero padding")
for i, (N_zero, X_zero, f_zero) in enumerate(zip(N_zeros, X_zeros, f_zeros)):
    plt.subplot(6, 1, i+2)
    plt.plot(f_zero, X_zero)
    plt.xlim([0, 10])
    plt.title(f"{N_zero} zero padding")
plt.tight_layout()
plt.show()
