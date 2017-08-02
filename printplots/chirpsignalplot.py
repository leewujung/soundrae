
# Plots a chirp signal, it's discrete fourier transform, and it's spectrogram.

import numpy as np
from scipy.signal import chirp
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab


time = np.linspace(0.0, 0.01, 2000)
chirp = chirp(time, f0=65.0e3, f1=35.0e3, t1=0.01, method='linear')

samples = len(chirp)

frequencies = np.fft.fftfreq(2000, d = 1 / 2000.0e3)
chirp_transform = np.fft.fft(chirp)

def sum_of_squares(function):
    return np.sum(function ** 2)

chirp_sum = sum_of_squares(chirp)
fourier_sum = sum_of_squares(np.abs(chirp_transform)) / samples
print(chirp_sum)
print(fourier_sum)

fig = plt.figure(figsize=(10,5))

ax1 = fig.add_subplot(3, 1, 1)
ax2 = fig.add_subplot(3, 1, 2)
ax3 = fig.add_subplot(3, 1, 3)

ax1.plot(time, chirp)
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Amplitude')

ax2.plot(frequencies / 10000, np.abs(chirp_transform) / samples)
ax2.set_xlabel('Frequency (khz)')
ax2.set_ylabel('Power')

ax3.specgram(chirp, NFFT=200, noverlap=0, Fs = 200.0e3,
             window=mlab.window_none)
ax3.set_xlabel('Time (s)')
ax3.set_ylabel('Frequency (hz)')

plt.show()
