import runpod
import subprocess
import requests
import time

def check_api_availability(host):
    while True:
        try:
            response = requests.get(host)
            return
        except requests.exceptions.RequestException as e:
            print(f"API is not available, retrying in 200ms... ({e})")
        except Exception as e:
            print('something went wrong')
        time.sleep(3)

check_api_availability("http://127.0.0.1:3000/sdapi/v1/txt2img")

print('run handler')

def handler(event):
    '''
    This is the handler function that will be called by the serverless.
    '''
    print('got event')
    print(event)

    if event["input"]["api_type"] == "txt2img":
        response = requests.post(url=f'http://127.0.0.1:3000/sdapi/v1/txt2img', json=event["input"])
    elif event["input"]["api_type"] == "img2img":
        response = requests.post(url=f'http://127.0.0.1:3000/sdapi/v1/img2img', json=event["input"])
    elif event["input"]["api_type"] == "sd-models":
        response = requests.get(url=f'http://127.0.0.1:3000/sdapi/v1/sd-models', json=event["input"])
    elif event["input"]["api_type"] == "options":
        response = requests.post(url=f'http://127.0.0.1:3000/sdapi/v1/options', json=event["input"]["options"])
    elif event["input"]["api_type"] == "refresh-checkpoints":
        response = requests.post(url=f'http://127.0.0.1:3000/sdapi/v1/refresh-checkpoints', json=event["input"])

    json = response.json()
    # do the things

    print(json)

    # return the output that you want to be returned like pre-signed URLs to output artifacts
    return json


runpod.serverless.start({"handler": handler})
