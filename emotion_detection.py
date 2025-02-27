'''
This module contains an emotion analyzer function which uses Watson API
'''
import json
import requests

def emotion_detector(text_to_analyze):
    """
    This function returns sentiment by using the Watson BERT sentiment analysis API
    """
    # URL of the emotion analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Custom header specifying the model ID for the sentiment analysis service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json=myobj, headers=header, timeout=10)

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # Returning a dictionary containing sentiment analysis results
    return formatted_response
