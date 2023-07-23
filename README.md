# Audio to text AI

Audio to text REST API using Faster Whisper

## Installation

Install dependencies

```sh
pip install -r builder/requirements.txt
```

Download models

```sh
python builder/fetch_models.py
```

### Using docker

Create docker image

```sh
docker build -t <image_name> .
```
