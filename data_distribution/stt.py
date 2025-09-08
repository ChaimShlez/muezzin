from faster_whisper import WhisperModel


class Stt:
    @staticmethod
    def speach_to_text(path):

        model = WhisperModel("base", device="cpu", compute_type="int8")
        segments, info = model.transcribe(path, beam_size=5)

        text=""
        for seg in segments:

            text+=seg.text
        return text

            # print(line, end="")




