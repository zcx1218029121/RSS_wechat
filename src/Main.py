# -*- coding: UTF-8
from wxpy import *
from providers.Provider import *
import json
import re
from pipe.Pipe import Pipe
import time

__author__ = "短狐"
cache = {}  # cache 字典对象
bot = Bot(cache_path=True)
map = {}  # 消息源
fd = []  # 订阅者


def init_config():
    f = open('../config.json', 'r', encoding='UTF-8')  # make sure utf-8
    job = json.loads(f.read())
    data = job['source']
    sb = job['subscriber']

    # initsource
    f.close()
    for temp in data:
        map[temp['msg']] = temp

    # init   friend
    for f in sb:
        fd.append(bot.friends().search(f['name'])[0])


def delAllHtml(context):
    return re.sub(r"</?(.+?)>", "", context)


def doReply(msg, cd=delAllHtml):
    s = ""
    try:
        p = Provider(map[msg]
                     ['url'], item=map[msg]['size'], cd=cd).score

        for j in p:
            if map[msg]['des'] == 0:
                s += j.title + j.link + "\n"
            else:
                s += j.title + j.context + j.link + "\n"

        return s

    except KeyError:
        KeyError.args
        return


@bot.register(fd)
def reply_my_friend(msg):
    if msg.text in map:
        return '{} '.format(doReply(msg.text))
    else:
        return


if __name__ == "__main__":
    # init_config()
    pip = Pipe(providers=Provider('https://rsshub.app/xueqiu/user/8152922548', item=5), valid_time=1)
    pip.get_date()
    pip.get_date()
    pip.get_date()
    time.sleep(20)
    pip.get_date()
