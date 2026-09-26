import wave
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from dft import dft

with wave.open("440Hz.wav", "r") as wav:
    audio_type = wav.getnchannels()   # How many channels?
    sample_width = wav.getsampwidth() # How big are the bins?
    sample_rate = wav.getframerate()  # Sample Rate?
    num_frames = wav.getnframes()     # How many samples?

    frames = wav.readframes(num_frames) # Create a variable holding the samples

signal = np.frombuffer(frames, dtype=np.int16) # take the samples and turn them into a numpy vector
signal = signal.astype(np.float64) / 32768.0   # Normalize the vector (-32768 is largest 16-bit signed int)

output = dft(signal[:1024])

N_of_F = len(output)
freq = np.arange(N_of_F) * sample_rate / N_of_F

plt.plot(freq[:N_of_F // 2], np.abs(output[:N_of_F // 2]))
plt.xlabel("Frequency (Hz)")
plt.ylabel("Intensity")
plt.show()

# ## Testing ##
# print(signal[:10])
# print(f"Channels: {audio_type}")
# print(f"Sample Width: {sample_width} bytes")
# print(f"Sample Rate: {sample_rate} Hz")
# print(f"Frames: {num_frames}")
# print(signal.shape)

    
    




