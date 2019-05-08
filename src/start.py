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
# TODO 实现pipe组件 （消息）--》（管道组件）---》返回  在管道组件内实现缓存 消息保存 文件保存  组装返回值等功能
# TODO 实现scene组件 组件结构 scene(pip(Usecache,FileType,),provider("msg",cd)).doReply() 场景组件负责对每个回复的组合装


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
    drs = ""
    try:
        p = provider(map[msg]
                     ['url'], item=map[msg]['size'], cd=cd).score

        for j in p:
            drs = drs.join([j.title, j.context, j.context])
        return drs

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
    # print(sb[0]['name'])
    # for i in fd:
    #   i.send('吃饭了')
embed()
