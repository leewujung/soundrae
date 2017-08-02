import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

fig = plt.figure(figsize=(25,5))

axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

## Generating a plot for a 65-35 linear chirp signal

f_init = 65e3
f_final = 35e3

t = np.linspace(0, 0.01, 1000)
k = 35e3 - 65e3 / 0.25
y = np.sin(2 * np.pi * (65e3 * t + (k / 2 * t ** 2)))

axes1.plot(t, y)
axes3.specgram(y, NFFT=256,noverlap=0,Fs = 150e3, window=mlab.window_none)
y_f = np.fft.fft(y)
freq = np.fft.fftfreq(1000, d = 1 / 150e3)

axes2.plot(freq, np.abs(y_f))
plt.show()
