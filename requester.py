"""requester.py module sends POST result to API ENDPOINT and gets response back"""
import requests
import json
import test_logger as tl


def send_payload(endpoint_url, payload_string):
    res = requests.get(url=endpoint_url, params=json.loads(payload_string))
    tl.test_logger.info('Payload: ' + payload_string)
    api_response_code = res.status_code    
    api_response_text = res.text
    api_response = [api_response_code, api_response_text]
    return api_response
