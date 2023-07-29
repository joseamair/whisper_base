import whisper
import json
import os
import pprint


def validate_model_selection(model):
    if model not in ['tiny','base','small','medium','large']:
        raise Exception("Wrong model selection: {}".format(model))
    else:
        pass

def transcribe(filepath, model_size="base", transcribe=True, get_language=True, verbose=False):

    validate_model_selection(model_size)

    w_result = {}

    if not os.path.isfile(filepath):
        return False, w_result

    # load model
    model = whisper.load_model(model_size)

    # Get the transcription from the audio Only
    if not get_language and transcribe:
        result = model.transcribe(filepath)
        w_result["transcript"] = result["text"]
        if verbose:
            pprint.pprint(w_result)
    
    else:
        # load audio and pad/trim it to fit 30 seconds
        audio = whisper.load_audio(filepath)
        audio = whisper.pad_or_trim(audio)

        # make log-Mel spectrogram and move to the same device as the model
        mel = whisper.log_mel_spectrogram(audio).to(model.device)

        # detect the spoken language
        _, probs = model.detect_language(mel)
        # print(f"Detected language: {max(probs, key=probs.get)}")

        # decode the audio
        options = whisper.DecodingOptions()
        result = whisper.decode(model, mel, options)

        w_result["transcript"] = result.text
        w_result["no_speech_prob"] = result.no_speech_prob
        w_result["language"] = f"{max(probs, key=probs.get)}"

        if verbose:
            pprint.pprint(w_result)
            
    return True, w_result