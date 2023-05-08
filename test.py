import re

import librosa
import numpy as np
import soundfile as sf

y, sr = sf.read("/home/hyeongikim/Desktop/음성인식/soundDataset/concatData/heongi.wav")

f = open("./result.txt", "r")
y0 = np.array([0])
y1 = np.array([0])
y2 = np.array([0])
y3 = np.array([0])
y4 = np.array([0])
y5 = np.array([0])

lines = f.readlines()
for line in lines:
    numbers = re.findall(r"\d+[.]\d", line)
    numbers = list(map(float, numbers))
    s1, s2 = int(numbers[0] * sr), int(numbers[1] * sr)
    print(s1, s2)
    if line[-2] == "0":
        y0 = np.concatenate([y0, y[s1:s2]])
    elif line[-2] == "1":
        y1 = np.concatenate([y1, y[s1:s2]])
    elif line[-2] == "2":
        y2 = np.concatenate([y2, y[s1:s2]])
    elif line[-2] == "3":
        y3 = np.concatenate([y3, y[s1:s2]])
    elif line[-2] == "4":
        y4 = np.concatenate([y4, y[s1:s2]])
    elif line[-2] == "5":
        y5 = np.concatenate([y5, y[s1:s2]])


sf.write("./speaker0" + ".wav", y0, sr, format="WAV")
sf.write("./speaker1" + ".wav", y1, sr, format="WAV")
sf.write("./speaker2" + ".wav", y2, sr, format="WAV")
sf.write("./speaker3" + ".wav", y3, sr, format="WAV")
sf.write("./speaker4" + ".wav", y4, sr, format="WAV")
sf.write("./speaker5" + ".wav", y5, sr, format="WAV")
