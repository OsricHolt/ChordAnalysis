import numpy as np
import wave
import matplotlib.pyplot as plt

sample_rate = 41000
frequency = 440
duration = 2.0
amplitude = 0.5


num_samples = sample_rate * duration # calculate num of sample in wav file
timestep = np.arange(num_samples) / sample_rate # generate a vector ennum by num of samples and scale to time

# ## Notes
# C = amplitude * np.sin(2 * np.pi * 261.63 * 2 * timestep) # multiply constants and apply sin to the vector
# E = amplitude * np.sin(2 * np.pi * 329.63 * 2 * timestep) # multiply constants and apply sin to the vector
# G = amplitude * np.sin(2 * np.pi * 392.00 * 2 * timestep) # multiply constants and apply sin to the vector


signal = amplitude * np.sin(2 * np.pi * frequency * timestep) # multiply constants and apply sin to the vector
# signal = C + E + G # add 3 notes into one signal to make a chord
signal_int = np.int16(signal * 32767) # scale values to 16 bit integers

## Converting to a WAV file

with wave.open("440Hz.wav", "w") as wav:
    wav.setnchannels(1) # set output to mono
    wav.setsampwidth(2) # set samplewidth to 2 bytes (16 bits)
    wav.setframerate(sample_rate) # set sample rate

    wav.writeframes(signal_int.tobytes()) # write the array values to each corresponding sample, converting to raw binary bytes



plt.plot(timestep[:500], signal[:500])
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.show()
