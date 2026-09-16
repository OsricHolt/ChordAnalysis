import wave
import numpy as np
import matplotlib as mpl

with wave.open("440Hz.wav", "r") as wav:
    audio_type = wav.getnchannels()
    sample_width = wav.getsampwidth()
    sample_rate = wav.getframerate()
    num_frames = wav.getnframes()

    frames = wav.readframes(num_frames)

signal = np.frombuffer(frames, dtype=np.int16)
signal = signal.astype(np.float64) / 32768.0


print(signal[:10])
# print(f"Channels: {audio_type}")
# print(f"Sample Width: {sample_width} bytes")
# print(f"Sample Rate: {sample_rate} Hz")
# print(f"Frames: {num_frames}")

    
    




