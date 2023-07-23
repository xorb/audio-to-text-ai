from whisper import Whisper
import json
import os

from flask import Flask

app = Flask(__name__)


@app.route('/')
def status():
    whisper = Whisper()
    transcript = whisper.transcribe("https://dl.sndup.net/fq8z/audio.mp3")
    return json.dumps(transcript)


@app.route('/', methods=['POST'])
def do_transcribe():
    whisper = Whisper()
    transcript = whisper.transcribe("https://dl.sndup.net/fq8z/audio.mp3")
    return json.dumps(transcript)


if __name__ == "__main__":
    if os.environ.get("FLASK_ENV") == "production":
        from waitress import serve
        serve(app, host="0.0.0.0", port=8080)
    else:
        app.run(host="0.0.0.0", port=8080, debug=True)
