import requests
from xml.etree import ElementTree
from domin.Iteam import *


def clear_date(context, mcd):
    if mcd is None:
        return context.replace(
            "<br/>", "\n").replace("<a href=", "").replace("</a>", "").replace(">", "")
    else:
        return mcd(context)


class Provider:

    def __init__(self, url, cd=None, item=1):
        self.__items = []
        self.url = url
        self.item = item
        self.cd = cd

    def getRequest(self):
        r = requests.get(self.url)
        print(r.status_code)
        if r.status_code == 200:
            return r
        else:
            return None

    def format(self, r):  # 解析Xml
        if r is None:
            return

        xml = r.text
        xml = ElementTree.fromstring(xml)
        items = xml[0].findall("item")
        for i in range(0, min(self.item, len(items) - 1)):
            title = items[i][0].text
            des = clear_date(items[i][1].text, mcd=self.cd)
            lk = items[i][4].text
            self.__items.append(Iteam(title, des, lk))

    @property
    # python的set 方法
    def score(self):
        # 清空数据
        self.__items.clear()
        self.format(self.getRequest())
        return self.__items
