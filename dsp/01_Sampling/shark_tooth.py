import numpy as np
import matplotlib.pyplot as plt

# Generate time array
fs = 200 # sampling rate
t = np.linspace(0, 2, 2*fs)

# Generate sinusoidal wave
f = 250 # frequency
x = np.sin(2*np.pi*f*t)

# Sampled the sinusoidal wave
fs_new = 100 # new sampling rate
t_new = np.linspace(0, 2, 2*fs_new)
x_sampled = np.sin(2*np.pi*f*t_new)

# Plot the original and sampled waves
plt.plot(t, x, label='Original')
plt.plot(t_new, x_sampled, 'o', label='Sampled')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Aliasing Example')
plt.legend()
plt.show()
