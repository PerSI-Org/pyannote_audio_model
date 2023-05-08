from glob import iglob

import numpy as np
import soundfile as sf

x = np.array([0])
for file in iglob(
    "/home/hyeongikim/Desktop/음성인식/soundDataset/hyeongi" + "/**" + "/*.wav",
    recursive=True,
):
    y, sr = sf.read(file)

    x = np.concatenate((x, y))
sf.write(
    "/home/hyeongikim/Desktop/음성인식/soundDataset/concatData/heongi.wav",
    x,
    sr,
    format="WAV",
)
