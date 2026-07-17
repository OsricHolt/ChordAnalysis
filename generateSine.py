import numpy as np
import wave
import matplotlib as mpl

sample_rate = 41000
frequency = 440
duration = 2
amplitude = 0.5

num_samples = sample_rate * duration # calculate num of sample in wav file
timestep = np.arrange(num_samples) / sample_rate # generate a vector ennum by num of samples and scale to time
signal = amplitude * np.sin(2 * np.pi * frequency * timestep)

mpl.pyplot.plot(t, signal)
mpl.pyplot.show()
