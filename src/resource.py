# -*- coding:utf-8 -*-
def search(barcode):
    if barcode == 'music':
        resource_id = '../resource/music.mp3'
        resource_type = 'music'
    elif barcode == 'video':
        resource_id = '../resource/video.mp4'
        resource_type = 'video'
    else:
        raise ResourceNotFound

    return resource_id, resource_type


def play(resource_id, resource_type):
    from subprocess import Popen
    import os

    proc = Popen(['omxplayer', resource_id])
    pgid = os.getpgid(proc.pid)

    return pgid


def terminate(pgid):
    import signal
    import os

    os.killpg(pgid, signal.SIGTERM)


class ResourceNotFound(Exception):
    pass


class ResourcePlayError(Exception):
    pass


if __name__ == '__main__':
    def my_job():
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
    t = threading.Thread(target=my_job)
    t.start()



