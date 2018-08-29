# -*- coding:utf-8 -*-
from subprocess import Popen, PIPE
import requests
import os
import json


def search(url):
    if url == 'music':
        meta_data = '../resource/music.mp3'
        # resource_type = 'music'
    # elif barcode == 'video':
        # meta_data = '../resource/video.mp4'
    else:
        p = Popen(['/Users/edwin/github/annie/annie', '-j', url], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate()
        if p.returncode == 0:
            output_array = json.loads(output)
            meta_data = dict()
            meta_data['site'] = output_array['Site']
            meta_data['title'] = output_array['Title']
            meta_data['origin'] = url
            meta_data['type'] = output_array['Type']
            meta_data['default'] = dict()
            meta_data['default'] = output_array['Formats']['default']
            return meta_data
        else:
            print(err.decode('utf8'))
            raise ResourceNotFound
    # else:
    #     raise ResourceNotFound

    return meta_data


def play(url):
    proc = Popen(['omxplayer', url])
    pgid = os.getpgid(proc.pid)

    return pgid


def terminate(pgid):
    import signal
    import os

    os.killpg(pgid, signal.SIGTERM)


def fetch(meta_data):
    # fifo = open('resource.fifo', 'wb')
    urls = meta_data['default']['URLs']
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 ' \
                 '(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    headers = {
        'user-agent': user_agent,
        'Referer': meta_data['origin']
    }

    with open('media.fifo', 'wb') as fd:
    # with open('1.mp4', 'wb') as fd:
        for URL in urls:
            url = URL['URL']
            print(url)
            r = requests.get(url, headers=headers, stream=True)
            print('begin download')
            print()
            i = 0
            for chunk in r.iter_content(chunk_size=1024):
                i += 1
                print('\rdownload {}k......'.format(i), end='')
                fd.write(chunk)
                fd.flush()


class ResourceNotFound(Exception):
    pass


class ResourcePlayError(Exception):
    pass


if __name__ == '__main__':
    def my_job(pgid):
        sleep(3)
        omxplayer.pause()
        sleep(1)
        omxplayer.pause()
        sleep(2)
        omxplayer.pause()
        sleep(2)
        omxplayer.pause()
        sleep(2)
        omxplayer.status()

        sleep(3)
        terminate(pgid)

    from time import sleep
    import threading
    import omxplayer

    pgid = play('../resource/music.mp3', 'music')
    # t1 = threading.Thread(target=play, args=['../resource/music.mp3', 'music'])
    # t1.start()

    t2 = threading.Thread(target=my_job, args=[pgid])
    t2.start()



