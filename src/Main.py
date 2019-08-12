# -*- coding: UTF-8
from wxpy import *
from providers.Provider import *
import json
import re
from pipe.Pipe import Pipe
import time

__author__ = "短狐"

bot = Bot(cache_path=True)
map = {}  # 消息源
fd = []  # 订阅者
providers = {}  # 数据提供者字典 用的是懒加载用到的时候再加载避免浪费RAM
cacheTime = 0
pip = Pipe(valid_time=60 * 60 * 2)


def init_config():
    f = open('../config.json', 'r', encoding='UTF-8')  # make sure utf-8
    job = json.loads(f.read())
    data = job['source']
    sb = job['subscriber']
    cache_time = job['cacheTime']

    f.close()
    read_source(data)
    read_subscriber(sb)
    init_pip(cache_time)


# clear html
def clear_content(context):
    return re.sub(r"</?(.+?)>", "", context)


# 读取订阅源
def read_source(data):
    for temp in data:
        map[temp['msg']] = temp


# 读取订阅者
# Param: sb 订阅者数组
def read_subscriber(sb):
    for f in sb:
        fd.append(bot.friends().search(f['name'])[0])


# 根据用户询问获取对应的url
def get_reply_url(msg):
    return map[msg]['url']


# 初始化数据提供者
def init_Provider(msg):
    return Provider(get_reply_url(msg), item=map[msg]['size'], cd=clear_content)


# parm:msg 用户回复
# return：返回数据提供者
# 获取数据提供者并初始化
def get_Provider(msg):
    if providers.__contains__(msg):
        return providers[msg]
    else:
        print("初始化数据提供者 ing .....")
        providers[msg] = init_Provider(msg)
        return providers[msg]


@bot.register(fd)
def reply_my_friend(msg):
    if msg.text in map:
        print(msg.text)
        return '{} '.format(pip.get_date(get_Provider(msg.text)))
    else:
        return


def init_pip(cache_time):
    pip = Pipe(cache_time)


if __name__ == "__main__":
    init_config()
    embed()
