# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
import requests
from scrapy import signals


class ZhihuSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

class MyCustomDownloaderMiddleware(object):
    ip = None

    # def __init__(self, crawler):
    #     self.crawler = crawler
    #
    #
    # @classmethod
    # def from_crawler(cls, crawler):
    #     return cls(crawler)

    # def process_response(self,request,response,spider):
    #     if response.status == 403:
    #         self.crawler.engine.close_spider(spider, 'closespider')
    #     return response

    def process_request(self, request, spider):
        if self.ip:
            request.meta['proxy'] = 'http://' + self.ip
        else:
            pass

    def process_response(self,request,response,spider):
        if response.status == 403:
            self.ip = self.get_proxy()
            request.meta['proxy'] = 'http://'+self.ip
            return request
        return response

    def get_proxy(self):
        try:
            response = requests.get('http://localhost:5555/random')
            if response.status_code == 200:
                return response.text
        except ConnectionError:
            return None
