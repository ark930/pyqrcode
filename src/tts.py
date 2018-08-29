# -*- coding: utf-8 -*-
import requests
import time
import hashlib
import base64
import json

URL = "http://api.xfyun.cn/v1/service/v1/tts"
AUE = "raw"     # lame/raw
APPID = "5b865c7f"
API_KEY = "5e370cca777ee85125d05abc2ace65fb"


def param_base64_encode(param):
    data = json.dumps(param).encode('utf-8')
    return base64.b64encode(data).decode('utf8')


def md5_checksum(content):
    md5 = hashlib.md5(content.encode('utf-8'))
    return md5.hexdigest()


def get_header():
    now = str(int(time.time()))
    param = {
        'aue': AUE,
        'auf': 'audio/L16;rate=16000',
        'voice_name': 'xiaoyan',
    }
    param_base64 = param_base64_encode(param)
    checksum = md5_checksum(API_KEY + now + param_base64)

    header = {
        'X-CurTime': now,
        'X-Param': param_base64,
        'X-Appid': APPID,
        'X-CheckSum': checksum,
        'X-Real-Ip': '127.0.0.1',
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'
    }
    return header


def get_body(text):
    data = {'text': text}
    return data


def write_file(file, content):
    with open(file, 'wb') as f:
        f.write(content)


def sentence_to_audio(sentence):
    r = requests.post(URL, headers=get_header(), data=get_body(sentence))
    content_type = r.headers['Content-Type']
    if content_type == "audio/mpeg":
        sid = r.headers['sid']
        extend_name = 'wav' if AUE == 'raw' else 'mp3'
        file_path = 'audio/{}.{}'.format(sid, extend_name)
        write_file(file_path, r.content)
        print("success, sid = " + sid, file_path)
        return file_path
    else:
        print(r.text)


if __name__ == '__main__':
    sentence = '欢迎来到地球'
    file_path = sentence_to_audio(sentence)
