from glob import iglob

from pydub import AudioSegment


def m4a_to_wav(dir):
    for file in iglob(dir + "/**" + "/*.m4a", recursive=True):

        m4a_file = file
        wav_filename = file[:-4] + ".wav"

        track = AudioSegment.from_file(m4a_file, format="m4a")
        file_handle = track.export(wav_filename, format="wav")
