'''
Sinc function we get we solving DFT by hand.
'''
import numpy as np
import matplotlib.pyplot as plt

N = 1000
f = 1005
fs = 10000
x = np.linspace(1, 600, 10000)
y = np.sin(np.pi*N*f/fs - np.pi * x) / np.sin(np.pi*f/fs - np.pi * x /N)

plt.plot(x, y)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Sinc')
plt.show()