'''
Frequency aliasing effect. 
This example sample a sinusoidal wave with sampling rate higher than Nyquist frequency. 
Then, it is sampled below Nyquist frequency. Then, the signal is reconstructed but with
a 7kHz frequency being aliased as a 1kHz when the signal is reconstructed.
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

fs = 10e6 # Sampling rate

# Original signal
f = 7000 # Signal frequency
T = 1/fs # Sampling interval
t = np.arange(0, 1, T) # Time array
x = np.sin(2 * np.pi * f * t) # Generating the signal

# Signal with frequency higher than Nyquist
fs_new = 6000 # New Sampling rate
T_new = 1/fs_new # New Sampling interval
t_new = np.arange(0, 1, T_new) # New Time array
x_resampled = np.interp(t_new, t, x) # Resampled signal

#reconstruct signal
t_r = np.arange(0, 1, T)
spl = CubicSpline(t_new, x_resampled)


plt.figure(figsize=(10, 7))
plt.suptitle('Digital filter frequency response')
plt.subplot(2, 1, 1)

plt.plot(t, x) # Plotting the time-domain signal
plt.xlim([0, 0.01])
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Signal in Time Domain')
plt.axvline(1/f, color='green',alpha=0.4)
plt.axvline(2*(1/f), color='green',alpha=0.4)

plt.subplot(2, 1, 2)
plt.plot(t_new, x_resampled,'o', label='Sampled signal')
plt.plot(t_r, spl(t_r),'-.', label='Reconstructed signal')
plt.xlim([0, 0.01])
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Resampled Signal in Time Domain')
plt.axvline(0.000500, color='green',alpha=0.4) 
plt.axvline(0.001500, color='green',alpha=0.4) 
plt.grid(True,which='both')

plt.tight_layout()
plt.show()