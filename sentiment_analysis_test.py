"""Sentiment analysis function"""
import json
import requests

def sentiment_analyzer(text_to_analyze):
    """function to perform sentiment analysis"""
    url = ("https://sn-watson-sentiment-bert.labs.skills.network/"
           "v1/watson.runtime.nlp.v1/NlpService/SentimentPredict")
    headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=headers, timeout = 7)
    print(response.status_code)
