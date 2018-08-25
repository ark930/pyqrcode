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
    from subprocess import call
    call(['omxplayer', resource_id])
    # call(['echo', resource_id])
    # pid = call(['sleep', '3'])
    # print(pid)
    # raise ResourcePlayError


class ResourceNotFound(Exception):
    pass


class ResourcePlayError(Exception):
    pass
