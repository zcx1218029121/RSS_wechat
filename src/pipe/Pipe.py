import time


# 数据格式化
def format_context(items):
    context = ""
    try:
        for item in items:
            context += item.title + item.context + item.link + "\n"
        return context
    except KeyError:
        print(KeyError.args)
        return "解析失败，请稍后再试"


class Pipe:
    # 回复数据的组装
    # 抓取数据的持久化
    # 抓取内容的缓存 当前只实现了二级缓存
    def __init__(self, providers, valid_time=0):
        # 缓存的有效时间 单位秒
        self.valid_time = valid_time
        # 内存的缓存字典
        self._cache = {}
        # 数据提供类
        self._provider = providers

    # 获取数据缓存
    # date
    def get_date(self):
        url = self._provider.url
        if self._cache.__contains__(url):
            # 检查缓存是否存在
            temp_cache_item = self._cache[url]
            if temp_cache_item['un_valid_time'] > time.time():
                print("从缓存中获取")
                return temp_cache_item['context']
            else:
                return self.update_cache(url)
        else:
            return self.update_cache(url)

    def update_cache(self, url):
        print("内存缓存被击穿")
        contexts = format_context(self._provider.score)

        cache_item = {'context': contexts, 'un_valid_time': time.time() + self.valid_time}
        self._cache[url] = cache_item
        return contexts
