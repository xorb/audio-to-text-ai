from whisper import Whisper
import json
import os

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['POST'])
def transcribe():
    data = request.get_json()

    if 'url' not in data:
        return jsonify({'error': 'URL not found in the request body'}), 400

    url = data['url']

    whisper = Whisper()
    transcript = whisper.transcribe(url)

    return json.dumps(transcript)


if __name__ == "__main__":
    if os.environ.get("FLASK_ENV") == "production":
        from waitress import serve
        serve(app, host="0.0.0.0", port=8080)
    else:
        app.run(host="0.0.0.0", port=8080, debug=True)
