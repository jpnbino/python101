import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, CubicSpline

# Sample rate and signal frequency
fs = 2 # Hz
f = 1 # Hz

# Time vector
T = 1 # sec
t = np.arange(0, 10, T) # Time array

# Sampled signal
x = np.sin(2 * np.pi * f * t)

# Interpolation function
spl = CubicSpline(t, x)

# Interpolated time vector
t_interp = np.linspace(0, T, int(fs*100), endpoint=False)

# Interpolated signal
x_interp = spl(t_interp)

# Plot
plt.plot(t, x, 'o', label='Sampled signal')
plt.plot(t_interp, x_interp, label='Interpolated signal')
plt.legend()
plt.show()
