import json
import requests as req
from dotenv import load_dotenv, dotenv_values
import os


load_dotenv()
COBALT_URL = os.getenv('COBALT_URL')
COBALT_URL_PORTLESS = os.getenv('COBALT_URL_PORTLESS')
PROXIES = {
    'http': os.getenv('SALAD_HTTP_PROXY'),
    'https': os.getenv('SALAD_HTTPS_PROXY')
}

def cobalt_get_files(req_link : str):

    request = {}
    request['url'] = COBALT_URL
    request['headers'] = { 'Accept': 'application/json',
                           'Content-Type': 'application/json' }
    request['body'] = { 'url': req_link }
    
    response = req.post(request['url'], headers=request['headers'], json=request['body'])
    response_json = response.json()
    print(response_json)
    
    if response_json['status'] == 'tunnel':
        resp_urls = response_json['url']
        crop_i = resp_urls.find(COBALT_URL_PORTLESS) + len(COBALT_URL_PORTLESS)
        resp_urls = COBALT_URL + resp_url[crop_i:]
    
    elif response_json['status'] == 'redirect':
        resp_urls = response_json['url']
    
    elif response_json['status'] == 'picker':
        resp_urls = [ pick['url'] for pick in response_json['picker'] ]
    
    else: # error response
        return []
    
    if type(resp_urls) != list:
        resp_urls = [resp_urls]
    
    fnames = []
    for resp_url in resp_urls:
        file_response = req.get(resp_url, proxies=PROXIES)
        
        fname = response_json['filename']
        file = open(fname, 'wb')
        file.write(file_response.content)
        file.close()
    
        fnames.append(fname)

    return fnames


res = cobalt_get_files(input())
print(res)

