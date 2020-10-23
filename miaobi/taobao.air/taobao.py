# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)

if exists(Template(r"tpl1603420779218.png", record_pos=(0.346, 0.758), resolution=(1080, 2340))):
    touch(Template(r"tpl1603420779218.png", record_pos=(0.346, 0.758), resolution=(1080, 2340)))
    sleep(5)
    
    while True:


        if exists(Template(r"tpl1603420866325.png", record_pos=(0.322, 0.106), resolution=(1080, 2340))):
            touch(Template(r"tpl1603420866325.png", record_pos=(0.322, 0.106), resolution=(1080, 2340)))
            sleep(25)
            keyevent("BACK")
            sleep(3)
        elif exists(Template(r"tpl1603421009727.png", record_pos=(-0.011, 0.024), resolution=(1080, 2340))):
            touch(exists(Template(r"tpl1603421023601.png", record_pos=(-0.074, 0.194), resolution=(1080, 2340))))
        elif exists(Template(r"tpl1603421830613.png", record_pos=(0.029, -0.194), resolution=(1080, 2340))):
            touch(Template(r"tpl1603421830613.png", record_pos=(0.029, -0.194), resolution=(1080, 2340)))
            sleep(1)
        elif exists(Template(r"tpl1603422724352.png", record_pos=(0.323, 0.281), resolution=(1080, 2340))):
            touch(Template(r"tpl1603422724352.png", record_pos=(0.323, 0.281), resolution=(1080, 2340)))
            sleep(25)
            keyevent("BACK")
            sleep(3)
            
        elif exists(Template(r"tpl1603436604189.png", record_pos=(0.005, 0.968), resolution=(1080, 2340))):
            touch(Template(r"tpl1603436604189.png", record_pos=(0.005, 0.968), resolution=(1080, 2340)))
            sleep(5)
        else:
            break
