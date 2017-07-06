
# Plots a sine signal, it's discrete fourier transform, and it's spectrogram

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

sample_frequency = 100e3
sample_interval = 1 / sample_frequency
samples = 1000
signal_frequency = 35e3

time = np.linspace(0, samples * sample_interval, samples)
signal = np.sin(2 * np.pi * signal_frequency * time)

signal_spectrum = np.fft.fftshift(np.fft.fft(signal))
frequencies = np.fft.fftshift(np.fft.fftfreq(samples, d=sample_interval))

parseval_1 = np.sum(signal ** 2)
parseval_2 = np.sum(np.abs(signal_spectrum ** 2)) / samples
print(parseval_1)
print(parseval_2)

fig = plt.figure(figsize=(25,5))

axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

axes1.plot(time, signal)
axes1.set_xlabel('Time (s)')
axes1.set_ylabel('Amplitude')

axes2.plot(frequencies / 1000, np.abs(signal_spectrum) / samples)
axes2.set_xlabel('Frequency (khz)')
axes2.set_ylabel('Power')

axes3.specgram(signal, NFFT=256, noverlap=0, Fs = sample_frequency,
               window=mlab.window_none)
axes3.set_xlabel('Time (s)')
axes3.set_ylabel('Frequency (hz)')

plt.show()
