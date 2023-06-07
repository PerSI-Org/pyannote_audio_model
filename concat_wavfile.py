from glob import iglob

import numpy as np
import soundfile as sf


def concat_all_file(input_dir, output_dir, filename):
    x = np.array([0])
    for file in iglob(
        input_dir + "/**" + "/*.wav",
        recursive=True,
    ):
        y, sr = sf.read(file)

        x = np.concatenate((x, y))
    target_file = output_dir + "/" + filename + ".wav"
    sf.write(
        target_file,
        x,
        sr,  # 16000
        format="WAV",  # flac
    )
    return target_file
