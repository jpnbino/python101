import numpy as np
import matplotlib.pyplot as plt

# Generate a signal with 10 samples
x = np.array([1,2,3,4,5,6,7,8,9,10])

# Plot the original signal
plt.figure(figsize=(12, 8))
plt.stem(np.arange(10), x, 'r', label='Original signal')
plt.xlabel('Sample number')
plt.ylabel('Amplitude')
plt.legend()
plt.title('Original signal in time domain')
plt.show()

# Plot the zero-padded signals in frequency domain
for n in [10, 32, 64, 128, 512, 1024]:
    X = np.fft.fft(x, n=n)
    plt.figure(figsize=(12, 8))
    plt.stem(np.arange(n), np.abs(X), 'r', label='Zero-padded DFT')
    plt.xlabel('Sample number')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.title(f'Zero-padded DFT, n={n}')
    plt.show()
