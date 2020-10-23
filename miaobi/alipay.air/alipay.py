# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)

if exists(Template(r"tpl1603418770693.png", record_pos=(-0.005, 0.344), resolution=(1080, 2340))):
    touch(Template(r"tpl1603418770693.png", record_pos=(-0.005, 0.344), resolution=(1080, 2340)))

else:
    touch(Template(r"tpl1603416546228.png", record_pos=(0.362, 0.734), resolution=(1080, 2340)))
    sleep(5)

while True:
    if exists(Template(r"tpl1603418770693.png", record_pos=(-0.005, 0.344), resolution=(1080, 2340))):
        touch(Template(r"tpl1603418770693.png", record_pos=(-0.005, 0.344), resolution=(1080, 2340)))
        sleep(5)

    elif exists(Template(r"tpl1603418356229.png", record_pos=(0.323, 0.143), resolution=(1080, 2340))):
        touch(Template(r"tpl1603418356229.png", record_pos=(0.323, 0.143), resolution=(1080, 2340)))
        sleep(20)
        keyevent("BACK")
        sleep(10)
    else:
        break

# 跳转淘宝
if exists(Template(r"tpl1603419445473.png", record_pos=(0.003, 0.911), resolution=(1080, 2340))):
    touch(Template(r"tpl1603419445473.png", record_pos=(0.003, 0.911), resolution=(1080, 2340)))
    sleep(15)