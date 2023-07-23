from faster_whisper import WhisperModel


class Whisper:
    def __init__(self, model_size="base", device="cpu", compute_type="int8"):
        self.model_size = model_size
        self.device = device
        self.compute_type = compute_type

    def transcribe(self, url: str):
        model = WhisperModel(
            self.model_size, device=self.device, compute_type=self.compute_type)
        segments, info = model.transcribe(
            url, beam_size=5, word_timestamps=True)

        transcript = {}
        transcript['language'] = info.language
        transcript['language_probability'] = info.language_probability

        data = []
        for segment in segments:
            segment_json = {}
            segment_json['start'] = segment.start
            segment_json['end'] = segment.end
            segment_json['text'] = segment.text
            segment_json['words'] = []
            for word in segment.words:
                segment_json['words'].append(
                    {"end": word.end, "start": word.start, "word": word.word})
            data.append(segment_json)

        # add segments to transcript
        transcript['data'] = data

        return transcript
