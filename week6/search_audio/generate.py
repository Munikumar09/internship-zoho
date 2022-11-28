import numpy as np
import wavio
import random
import string
from pathlib import Path
import os
def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


script_dir = os.path.dirname(__file__)
rate = 44100    # samples per second
T = 3           # sample duration (seconds)
f = 440.0       # sound frequency (Hz)
# Compute waveform samples
for i in range(10000):
    t = np.linspace(0, T, T*rate, endpoint=False)
    x = np.sin(2*np.pi * f * t)
    # Write the samples to a file
    file_name=get_random_string(10)+".wav"
    rel_path = f"audio/{file_name}"
    abs_file_path = os.path.join(script_dir, rel_path)
    with open(abs_file_path, 'wb') as ff:
        wavio.write(ff, x, rate, sampwidth=3)