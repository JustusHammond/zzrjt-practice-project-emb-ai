"""Sentiment analysis function"""
import json
import requests

def sentiment_analyzer(text_to_analyze):
    """function to perform sentiment analysis"""
    url = ("https://sn-watson-sentiment-bert.labs.skills.network/"
           "v1/watson.runtime.nlp.v1/NlpService/SentimentPredict")
    headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    payload = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = payload, headers=headers, timeout = 7)
    formatted_response = json.loads(response.text)
    label = formatted_response['documentSentiment']['label']
    score = formatted_response['documentSentiment']['score']

    return {'label': label, 'score': score}
