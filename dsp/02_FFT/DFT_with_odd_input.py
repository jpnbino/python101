'''
What is the condition for the symmetry of the DFT around the frequency sample divided by two?

The condition for the symmetry of the DFT around the frequency sample divided by two is that
the input signal must be real-valued and have even length. When the input signal satisfies these 
conditions, the magnitude of the DFT will be symmetric around the frequency sample divided by two.
This is known as the conjugate symmetry property of the DFT. The phase of the DFT will also exhibit 
symmetry under these conditions, with positive frequencies having the same phase as their corresponding
 negative frequencies.
'''
import numpy as np
import matplotlib.pyplot as plt

# Generate an odd length signal
N = 5
N2 = 6
x = np.sin(2 * np.pi * 0.3 * np.arange(N))
x2 = np.sin(2 * np.pi * 0.3 * np.arange(N2))
# Compute the DFT
X = np.fft.fft(x)
X2 = np.fft.fft(x2)
# Plot the magnitude of the DFT
plt.subplot(1, 2, 1)
plt.stem(np.abs(X),'red',label='odd')
plt.xlabel('Sample')
plt.ylabel('Magnitude')

plt.subplot(1, 2, 2)
plt.stem(np.abs(X2),label='even')
plt.axvline(N2/2, color='green',alpha=0.4,linestyle="--")
plt.tight_layout()
plt.show()
