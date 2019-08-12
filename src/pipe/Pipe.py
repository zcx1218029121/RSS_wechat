import time


# 数据格式化
# 数据缓存
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
    def __init__(self, valid_time=0):
        # 缓存的有效时间 单位秒
        self.valid_time = valid_time
        # 内存的缓存字典
        self._cache = {}



    def get_date(self,provider):
        url = provider.url
        # 检查缓存是否存在
        if self._cache.__contains__(url):
            temp_cache_item = self._cache[url]
            # 检查缓存是否超时
            if temp_cache_item['un_valid_time'] > time.time():
                print("从缓存中获取")
                return temp_cache_item['context']
        else:
            return self.update_cache(provider)

    def update_cache(self, provider):
        print("内存缓存被击穿")
        contexts = format_context(provider.score)
        cache_item = {'context': contexts, 'un_valid_time': time.time() + self.valid_time}
        self._cache[provider.url] = cache_item
        return contexts
