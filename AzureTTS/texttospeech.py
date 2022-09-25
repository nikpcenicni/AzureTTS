import os
import dotenv
import azure.cognitiveservices.speech as speechsdk



dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

SPEECH_KEY = os.environ['SPEECH_KEY']
SPEECH_REGION = os.environ['SPEECH_REGION']
SPEECH_SYNTHESIS_VOICE_NAME = os.environ['SPEECH_SYNTHESIS_VOICE_NAME']


def texttospeechOptions(text, speed, pitch):
    command = '<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-US">'
    command += '<voice name="{}">'.format(SPEECH_SYNTHESIS_VOICE_NAME)
    command += '<prosody rate="{}%" pitch ="{}%">'.format(speed, pitch)
    command += text
    command += '</prosody>'
    command += '</voice>'
    command += '</speak>'
    
    print(command)
    
    speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    
    speech_synthesis_result = speech_synthesizer.speak_ssml_async(command).get()
    if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized for text [{}]".format(text))
    elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")
