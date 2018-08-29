import json
import requests


def chat(sentence):
    api_url = "http://openapi.tuling123.com/openapi/api/v2"

    req = {
        "perception": {
            "inputText": {
                "text": sentence
            },
        },
        "userInfo": {
            "apiKey": "e3ffebafa6624c5fb47c8ac44a486acf",
            "userId": "OnlyUseAlphabet"
        }
    }

    req = json.dumps(req).encode('utf8')
    r = requests.post(api_url, headers={'content-type': 'application/json'}, data=req)
    response_dic = json.loads(r.text)

    intent_code = response_dic['intent']['code']
    results_text = response_dic['results'][0]['values']['text']
    print('Turing的回答：')
    print('code：' + str(intent_code))
    print('text：' + results_text)
    return results_text
