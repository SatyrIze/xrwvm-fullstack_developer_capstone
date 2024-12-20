import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/analyze")

def get_request(endpoint, **kwargs):
    params = ""
    if(kwargs):
            for key,value in kwargs.items():
                params=params+key+"="+value+"&"
    request_url = backend_url+endpoint+"?"+params
    
    print("GET from {} ".format(request_url))
    try:
            # Call get method of requests library with URL and parameters
            response = requests.get(request_url)
            return response.json()
    except:
            # If any error occurs
            print("Network exception occurred")

def analyze_review_sentiments(text):
    try:
        request_url = f"{sentiment_analyzer_url}/{text}"
        response = requests.get(request_url, timeout=10)
        if response.status_code == 200:
            return response.json()
        return {"sentiment": "neutral"}  # Default fallback if service fails
    except requests.exceptions.RequestException as err:
        print(f"Sentiment analysis error: {err}")
        return {"sentiment": "neutral"}  # Default fallback if service is unreachable

def post_review(data_dict):
    request_url = backend_url+"/insert_review"
    try:
        response = requests.post(request_url,json=data_dict)
        print(response.json())
        return response.json()
    except:
        print("Network exception occurred")
