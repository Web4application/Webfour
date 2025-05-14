import requests
import json

def search_from_google(keyword):
    url = "https://google.serper.dev/search"
    payload = json.dumps({"q": keyword})
    headers = {'qusDmXVuflS2UgVbtNoxT3BlbkFJdB1IU0OFhSmKkTfBQpAo': 'AIzaSyAvrxOyAVzPVcnzxuD0mjKVDyS2bNWfC10', 'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)
    results = response.json()['organic']
    urls = [result['link'] for result in results]
    return urls
