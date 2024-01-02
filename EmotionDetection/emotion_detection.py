import requests
import json

def emotion_predictor(formatted_response):
    '''
    Returns : emtions with the dominant one as a dict
    '''
    emotions = formatted_response["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(emotions, key=emotions.get)
    emotions["dominant_emotion"] = dominant_emotion
    return emotions

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(URL, json = myobj , headers = HEADERS)
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        emotions = emotion_predictor(formatted_response)
        return emotions
    elif response.status_code != 200:
        return {"message" : "sum ting wong"}


