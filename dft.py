import numpy as np
import wave
import matplotlib.pyplot as plt

def dft(signal):
    N = len(signal)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        total = 0
        for n in range(N):
            total += signal[n] * np.exp(-2j * np.pi * k * n / N)
        X[k] = total
    return X
