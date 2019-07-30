# TODO 管道类负责 数据的持久化 抓取内容的缓存
class Pipe:
    def __init__(self, items, cd=None, item=1):
        self.__items = items
        self.item = item
        self.cd = cd
