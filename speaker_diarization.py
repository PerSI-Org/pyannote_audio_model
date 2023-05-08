import soundfile as sf
from pyannote.audio import Pipeline
from pyannote.metrics.diarization import DiarizationErrorRate

metric = DiarizationErrorRate()

pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization",
    use_auth_token="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",
)
f = open("./result.txt", "w")
diarization = pipeline(
    "/home/hyeongikim/Desktop/음성인식/soundDataset/concatData/heongi.wav"
)
y, sr = sf.read("/home/hyeongikim/Desktop/음성인식/soundDataset/concatData/heongi.wav")

for turn, _, speaker in diarization.itertracks(yield_label=True):
    print(f"start={turn.start:.1f}s stop={turn.end:.1f}s speaker_{speaker}", file=f)
