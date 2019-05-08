# -*- coding: UTF-8 -*-
from wxpy import *
from provider.Provider import *
import json

__author__ = "短狐"

bot = Bot(cache_path=True)
map = {}  # 消息源
fd = []  # 订阅者
# 当前版本只提供简单的回复功能
# TODO 缓存功能
# TODO 实现pipe组件 （消息）--》（管道组件）---》返回  在管道组件内实现缓存 消息保存 文件保存等功能
# TODO 实现scene组件 组件结构 scene(pip(Usecache,FileType,),provider("msg")).doReply() 场景组件负责对每个回复的组合装


def cd1(context):
    return context


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


def doReply(provider):
    drs = ""
    try:
        p = provider.score
        for j in p:
            drs += j.title + j.context
        return drs
    except KeyError:
        KeyError.args


if __name__ == "__main__":
    initConfig()
   # print(doReply(provider(map['虎扑']
   #                        ['url'], item=map['虎扑']['size'])))

   # print(sb[0]['name'])
    for i in fd:
        i.send('吃饭了')
