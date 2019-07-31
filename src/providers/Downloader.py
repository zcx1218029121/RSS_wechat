# -*- coding: UTF-8 -*-
# 网络请求类负责网络请求 //虽然并用不到
import urllib.parse
import urllib.request
import random
import time
from datetime import datetime, timedelta
import socket

DEFAULT_AGENT = 'wswp'
DEFAULT_DELAY = 0
DEFAULT_RETRIES = 1
DEFAULT_TIMEOUT = 60
DEFAULT_HEADER = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}


class Downloader:
    def __init__(self, delay=DEFAULT_DELAY, user_agent=DEFAULT_AGENT, proxies=None,
                 num_retries=DEFAULT_RETRIES, timeout=DEFAULT_TIMEOUT, opener=None, cache=None):
        socket.setdefaulttimeout(timeout)
        self.throttle = Throttle(delay)
        self.user_agent = user_agent
        self.proxies = proxies
        self.num_retries = num_retries
        self.opener = opener
        self.cache = cache

    def __call__(self, url):
        result = None
        if self.cache:
            try:
                result = self.cache[url]
            except KeyError:
                # url is not available in cache
                pass
            else:
                if self.num_retries > 0 and 500 <= result['code'] < 600:
                    # server error so ignore result from cache and re-download
                    result = None
        if result is None:
            # result was not loaded from cache so still need to download

            proxy = random.choice(self.proxies) if self.proxies else None
            headers = {'User-agent': self.user_agent}
            result = self.download(
                url, headers, proxy=proxy, num_retries=self.num_retries)
            if self.cache:
                # save result to cache
                self.cache[url] = result
        return result['html']

    def download(self, url,  num_retries, data=None, headers=DEFAULT_HEADER, proxy=None):
        print('Downloading:', url)
        self.throttle.wait(url)
        request = urllib.request.Request(url, data, headers or {})
        opener = self.opener or urllib.request.build_opener()
        self.throttle.wait(url)
        if proxy:
            proxy_params = {urllib.parse.urlparse(url).scheme: proxy}
            opener.add_handler(urllib.request.ProxyHandler(proxy_params))
        try:
            response = opener.open(request)
            html = response.read().decode('utf-8')
            code = response.code
        except Exception as e:
            print('Download error:', str(e))
            html = ''
            if hasattr(e, 'code'):
                code = e.code
                if num_retries > 0 and 500 <= code < 600:
                    # retry 5XX HTTP errors
                    return self.download(url, headers, proxy, num_retries - 1, data)
            else:
                code = None
        return {'html': html, 'code': code}


class Throttle:
    """Throttle downloading by sleeping between requests to same domain
    """

    def __init__(self, delay):
        # amount of delay between downloads for each domain
        self.delay = delay
        # timestamp of when a domain was last accessed
        self.domains = {}

    def wait(self, url):
        """Delay if have accessed this domain recently
        """
        domain = urllib.parse.urlsplit(url).netloc
        last_accessed = self.domains.get(domain)
        if self.delay > 0 and last_accessed is not None:
            sleep_secs = self.delay - (datetime.now() - last_accessed).seconds
            if sleep_secs > 0:
                time.sleep(sleep_secs)
        self.domains[domain] = datetime.now()


if __name__ == "__main__":
    for i in range(0, 2):
        print(Downloader().download(url="https://rsshub.app/hupu/bbs/bxj/2",
                                    proxy=None, num_retries=1))
