from faster_whisper import WhisperModel


class Transcription:


     @staticmethod
     def speach_to_text(audio_data):
         model = WhisperModel("base", device="cpu", compute_type="int8")
         segments, info = model.transcribe(audio_data, beam_size=5)


         text=""
         for seg in segments:
             text += seg.text
         return text















