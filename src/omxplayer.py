# -*- coding:utf-8 -*-
from subprocess import call

debuscontroll = './dbuscontrol.sh'


def status():
    call([debuscontroll, 'status'])


def pause():
    call([debuscontroll, 'pause'])


def stop():
    call([debuscontroll, 'stop'])


def volumeup():
    call([debuscontroll, 'volumeup'])


def volumedown():
    call([debuscontroll, 'volumedown'])