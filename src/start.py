# -*- coding: UTF-8 -*-
from wxpy import *
from provider.Provider import *
import json
import re

__author__ = "短狐"

bot = Bot(cache_path=True)
map = {}  # 消息源
fd = []  # 订阅者

# 当前版本只提供简单的回复功能
# TODO 缓存功能


def initConfig():
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
        p = provider(map[msg]
                     ['url'], item=map[msg]['size'], cd=cd).score

        for j in p:
            if(map[msg]['des'] == 0):
                s += j.title+j.link+"\n"
            else:
                s += j.title+j.context+j.link+"\n"

        return s

    except KeyError:
        KeyError.args
        return


@bot.register(fd)
def reply_my_friend(msg):
    if(msg.text in map):
        if(msg.text == "今天发生了什么？"):
            return '{} '.format(doReply(msg.text, cd=None))
        else:
            return '{} '.format(doReply(msg.text))
    else:
        return


if __name__ == "__main__":
    initConfig()

    embed()
