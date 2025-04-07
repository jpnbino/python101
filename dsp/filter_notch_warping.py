'''
Notch filter example. Shows what frequency warping is.
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, freqz,freqs, TransferFunction,bode,bilinear

# Filter design parameters in Hz
fs = 0.5
w0=0.7
f0=w0/2*np.pi
Q = 1 #Quality factor

#TF in s-domain
num = [1,0,w0**2]
den = [1, w0/Q, w0**2]
sys = TransferFunction( num, den)
w_an, mag, phase = bode(sys, n = np.logspace(-2, 1, 1000))


#TF in z-domain without pre-warping
num_z, den_z = bilinear(num, den, fs)
w_no, h_no = freqz(num_z, den_z, worN=np.logspace(-2,1, 1000))

#TF in z-domain with pre-warping
w0_p = 2*fs*np.tan(w0/(2*fs))
print(w0_p)
num_p = [1,0,w0_p**2]
den_p = [1, w0_p/Q, w0_p**2]
num_zp, den_zp = bilinear(num_p, den_p, fs)
w_p, h_p = freqz(num_zp, den_zp, worN=np.logspace(-2, 1, 1000))


# Plot magnitude 
plt.figure(figsize=(10, 7))
plt.suptitle('Digital filter frequency response')
plt.subplot(2, 1, 1)

plt.semilogx(w_an, mag, label='S-Domain')
plt.semilogx(w_no*fs, 20 * np.log10(np.abs(h_no)),linestyle="--", label='Warping effect')
plt.semilogx(w_p*fs, 20 * np.log10(np.abs(h_p)),linestyle="-.", label='pre-warping')

plt.axvline(500, color='green',alpha=0.4) # cutoff frequency
plt.axvline(1000, color='green',alpha=0.4) # cutoff frequency

plt.xscale('log')
plt.xlim([0, 2])
plt.ylim([-50, 1])
plt.xlabel('Frequency (rad/s)')
plt.ylabel('Amplitude (dB)')
plt.grid(True,which='both')

plt.legend()

#Plot phase responses
plt.subplot(2, 1, 2)
plt.plot(w_an, phase,   label='S-Domain')
plt.plot(w_no*fs, (180/np.pi)*np.angle(h_no), linestyle="--",  label='warping')
plt.plot(w_p*fs, (180/np.pi)*np.angle(h_p),   linestyle="-.", label='pre-warping')

plt.xscale('log')
plt.xlim([0, 2])
plt.ylim([-180, 180])

plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase (Deg)')
plt.grid(True,which='both')
plt.legend()

plt.tight_layout()
plt.show()