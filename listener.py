from faster_whisper import WhisperModel

class JarvisListener:
    def __init__(self): # Initialize the Whisper model
        self.model = WhisperModel("Tiny", device="cpu", compute_type="int8")

    def listen(self, audio_file): # Method to capture and transcribe audio input:
        segments, info = self.model.transcribe(audio_file, beam_size=5)
        text = "".join([segment.text for segment in segments])
        return text.strip()