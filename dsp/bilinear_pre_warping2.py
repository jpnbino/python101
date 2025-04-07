import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, freqz,freqs, TransferFunction,bode,bilinear



# Filter design parameters in Hz
fs = 15e3     # sample rate
f_c1 = 500    # lower cut-off frequency 
f_c2 = 1000   # upper cut-off frequency
w1 = 2*np.pi*f_c1
w2 = 2*np.pi*f_c2

#TF in s-domain
num = [1/w1,0]
den = [1/(w1*w2),(1/w1)+(1/w2),1]
sys = TransferFunction( num, den)
w_an, mag, phase = bode(sys, n = np.logspace(-1, 8, 1000))
f_an = w_an/(2*np.pi)

#TF in z-domain without pre-warping
num_z, den_z = bilinear(num, den, fs)
w_no, h_no = freqz(num_z, den_z, worN=np.logspace(-1, 8, 1000))
f_no = w_no * fs / (2 * np.pi)

#TF in z-domain with pre-warping
# The following formulas were hand-made from exam 02.12.2022
k1 = 1/np.tan(np.pi*f_c1/fs)
k2 = 1/np.tan(np.pi*f_c2/fs)

a0 = k1
a2 = -k1
b0 = 1+k1+k2+k1*k2
b1 = 2-2*k1*k2
b2 = 1-k1-k2+k1*k2
num = np.array([a0, 0, a2])
den = np.array([b0, b1,b2])
w_p, h_p = freqz(num, den, worN=np.logspace(-1, 8, 1000))
f_p = w_p * fs / (2 * np.pi)


# Plot magnitude 
plt.figure(figsize=(10, 7))
plt.suptitle('Digital filter frequency response')
plt.subplot(2, 1, 1)

plt.semilogx(f_an, mag, label='S-Domain')
plt.semilogx(f_no, 20 * np.log10(np.abs(h_no)),linestyle="--", label='No pre-warping')
plt.semilogx(f_p, 20 * np.log10(np.abs(h_p)),linestyle="-.", label='pre-warping')

plt.axvline(500, color='green',alpha=0.4) # cutoff frequency
plt.axvline(1000, color='green',alpha=0.4) # cutoff frequency

plt.xscale('log')
plt.xlim([10, 10e4])
plt.ylim([-50, 1])
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude (dB)')
plt.grid(True,which='both')

plt.legend()

#Plot phase responses
plt.subplot(2, 1, 2)
plt.plot(f_an, phase,   label='S-Domain',linestyle="--")
plt.plot(f_no, (180/np.pi)*np.angle(h_no), linestyle="--",  label='No pre-warping')
plt.plot(f_p, (180/np.pi)*np.angle(h_p),   linestyle="-.", label='pre-warping')

plt.axvline(500, color='green',alpha=0.4) # cutoff frequency
plt.axvline(1000, color='green',alpha=0.4) # cutoff frequency


plt.xscale('log')
plt.xlim([100, 10e4])
plt.ylim([-180, 180])

plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase (Deg)')
plt.grid(True,which='both')
plt.legend()

plt.tight_layout()
plt.show()