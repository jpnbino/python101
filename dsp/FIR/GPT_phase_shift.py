import numpy as np
import matplotlib.pyplot as plt

def low_pass_fir(N, f_c, fs):
    # Low-pass FIR filter design
    h = np.zeros(N+1)
    n = np.arange(-N/2, N/2 + 1)
    for i in range(len(n)):
        if n[i] == 0:
            h[i] = 2 * np.pi * f_c / fs
        else:
            h[i] = np.sin(2 * np.pi * f_c * n[i] / fs) / (np.pi * n[i])
    h = h * np.hamming(N + 1)
    return h

def apply_fir_filter(x, h):
    # Apply FIR filter
    y = np.convolve(x, h,'same')
    return y

fs = 44100 # sample rate
T = 1.0 / fs # sample period
f_c = 1000 # cutoff frequency
N = 100 # filter order

# time vector
t = np.arange(0, 2, T)

# signals
f1 = 750
f2 = 1000
x1 = np.cos(2 * np.pi * f1 * t)
x2 = np.cos(2 * np.pi * f2 * t)

# combine signals
x = x1 + x2

# design low-pass FIR filter
h = low_pass_fir(N, f_c, fs)

# apply FIR filter
y = apply_fir_filter(x, h)
print(x.shape)
print(y.shape)
# plot signals before and after passing the filter
plt.figure(figsize=(10,5))
plt.subplot(2,1,1)
plt.plot(t, x)
plt.xlim([0, 0.05])
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Input signal')

plt.subplot(2,1,2)
plt.plot(t, y)
plt.xlim([0, 0.05])
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Output signal')

plt.tight_layout()
plt.show()