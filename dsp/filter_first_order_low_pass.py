'''
This program compares the first order system 
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, freqz,freqs, bode, TransferFunction

# Filter design parameters in Hz
fs = 15e3     # sample rate
f_c1 = 500    # lower cut-off frequency 
f_c2 = 1000   # upper cut-off frequency 

num = np.array([2*np.pi*f_c2])
den = np.array([1, 2*np.pi*f_c2])

w, h = freqs(num, den,worN=np.logspace(-1, 6, 1000))
f = w/(2*np.pi)

sys = TransferFunction([2*np.pi*f_c2], [1, 2*np.pi*f_c2])
print(sys)

w2, mag, phase = bode(sys, n = np.logspace(-1, 6, 1000))
f2 = w2/(2*np.pi)
#====================================================
# Plot magnitude 
plt.figure(figsize=(10, 7))
plt.suptitle('First Order Low Pass')
plt.subplot(2, 1, 1)
plt.semilogx(f, 20 * np.log10(np.abs(h)), label='Hand')
plt.semilogx(f2, mag, label='Bode',linestyle="--")
plt.xlim([10, 10e4])
#plt.ylim([-50, 1])
plt.ylabel('Amplitude (dB)')
plt.grid(True,which='both')
plt.axvline(f_c2, color='green',alpha=0.4,linestyle="--") # cutoff frequency
plt.axhline(-3, color='green',alpha=0.4, linestyle="--") # 3dB
plt.legend()

#Plot phase responses
plt.subplot(2, 1, 2)
plt.semilogx(f, (180/np.pi)*np.angle(h),   label='Analog')
plt.semilogx(f2, phase,   label='Bode',linestyle="--")
plt.xlim([10, 10e4])
plt.ylim([-100, 10])
plt.axvline(f_c2, color='green',alpha=0.4, linestyle="--") # cutoff frequency
plt.axhline(-45, color='green',alpha=0.4, linestyle="--") # 45 degree angle
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase (Deg)')
plt.grid(True,which='both')
plt.legend()

plt.tight_layout()
plt.show()