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

    pipeline = Pipeline.from_pretrained(
        "pyannote/speaker-diarization",
        use_auth_token="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",
    )
    device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
    pipeline.to(device)
    diarization = pipeline(args.data_in)
    y, sr = sf.read(args.data_in)
    f = open("./result.txt", "w")
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        print(f"start={turn.start:.1f}s stop={turn.end:.1f}s speaker_{speaker}", file=f)
        s1, s2 = int(turn.start * sr), int(turn.end * sr)
        sf.write(
            args.data_out_dir
            + "/"
            + str(round(turn.start, 2))
            + "~"
            + str(round(turn.end, 2))
            + ".wav",
            y[s1:s2],
            16000,
            format="WAV",
        )

    f = open("./result.txt", "r")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data_in",
        default="data_in",
        help="target .wav file of sound data",
    )
    parser.add_argument(
        "--data_out_dir",
        default="data_out",
        help="Directory containing concat .wav of sound data",
    )

    main(parser)
