import argparse
import re

import numpy as np
import soundfile as sf
import torch
from pyannote.audio import Pipeline

from concat_wavfile import concat_all_file
from m4a_to_wav import m4a_to_wav


def main(parser):
    args = parser.parse_args()
    m4a_to_wav(dir=args.data_in_dir)
    target_file = concat_all_file(
        input_dir=args.data_in_dir,
        output_dir=args.data_out_dir,
        filename=args.concat_filename,
    )

    pipeline = Pipeline.from_pretrained(
        "pyannote/speaker-diarization",
        use_auth_token="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",
    )

    diarization = pipeline(target_file, num_speakers=6)

    f = open("./result.txt", "w")
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        print(f"start={turn.start:.1f}s stop={turn.end:.1f}s speaker_{speaker}", file=f)

    y, sr = sf.read(target_file)

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

    yy = [y0, y1, y2, y3, y4, y5]

    lenth = [len(y0), len(y1), len(y2), len(y3), len(y4), len(y5)]
    i = lenth.index(max(lenth))

    sf.write(target_file, yy[i], sr, format="WAV")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data_in_dir",
        default="data_in",
        help="Directory containing *.m4a of sound data",
    )
    parser.add_argument(
        "--data_out_dir",
        default="data_out",
        help="Directory containing concat .wav of sound data",
    )
    parser.add_argument(
        "--concat_filename", default="test_concat_file", help="name of .wav sound data"
    )
    parser.add_argument(
        "--data_collecting_method",
        default="submit_recorded_files",
        help="recording, submit_recorded_files",
    )

    main(parser)
