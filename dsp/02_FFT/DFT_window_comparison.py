import numpy as np
import matplotlib.pyplot as plt

def dft(x):
    N = len(x)
    X = []
    for k in range(N):
        sum = 0
        for n in range(N):
            sum += x[n] * np.exp(-2j * np.pi * n * k / N)
        X.append(sum)
    return np.array(X)

def window_types():
    # Rectangular Window
    rect_win = np.ones(N)
    
    # Hamming Window
    hamming_win = 0.54 - 0.46 * np.cos(2 * np.pi * np.arange(N) / (N - 1))
    
    # Hanning Window
    hanning_win = 0.5 - 0.5 * np.cos(2 * np.pi * np.arange(N) / (N - 1))
    
    # Blackman Window
    blackman_win = 0.42 - 0.5 * np.cos(2 * np.pi * np.arange(N) / (N - 1)) + 0.08 * np.cos(4 * np.pi * np.arange(N) / (N - 1))
    
    return rect_win, hamming_win, hanning_win, blackman_win

def plot_spectrum(x, win, title):
    X = np.abs(dft(x * win))
    freq = np.arange(N) * fs / N
    plt.stem(freq, X, 'r', )
    plt.title(title)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.show()

# Parameters
fs = 1000 # Sampling frequency
N = 256 # Number of samples
f1 = 100 # Frequency of the first signal
f2 = 50 # Frequency of the second signal

# Create the signal
t = np.arange(N) / fs
x = np.sin(2 * np.pi * f1 * t) + 0.5 * np.sin(2 * np.pi * f2 * t)

# Create the windows
rect_win, hamming_win, hanning_win, blackman_win = window_types()

# Plot the spectrums
plot_spectrum(x, rect_win, 'Rectangular Window')
plot_spectrum(x, hamming_win, 'Hamming Window')
plot_spectrum(x, hanning_win, 'Hanning Window')
plot_spectrum(x, blackman_win, 'Blackman Window')