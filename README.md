# whisper_base

Repository for  code snippets to use whisper AI model for TTS and ASR tasks

- OpenAI Whisper Webpage: https://openai.com/research/whisper
- OpenAI Github repository: https://github.com/openai/whisper

## Setup the repo

### Install dependencies

1. Create Python virtual environment

    ```bash
    # Create env
    python -m venv venv;

    # Activate env
    source venv/bin/activate;
    ```

2. Install requirements:

    ```bash
    pip install -r requirements.txt
    ```

## Run tests

In order to run tests for this repo Go the base of the directory and run on the CLI:

```bash
python -m unittest discover -s tests
```
