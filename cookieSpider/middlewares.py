# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
# from selenium import webdriver
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# from scrapy.http import HtmlResponse
# from logging import getLogger
import time


class CookiespiderSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class CookiespiderDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called

        # print(f"chrome is getting page")
        # 依靠meta中的标记，来决定是否需要使用selenium来爬取
        # usedSelenium = request.meta.get('usedSelenium', True)
        # if usedSelenium:
        #     try:
        #         spider.browser.get(request.url)
        #         # 判断是否为首页
        #         if "https://tieba.baidu.com/" == request.url:
        #             element = WebDriverWait(spider.browser, 10).until(EC.presence_of_element_located((By.XPATH, "//li[@class='u_login']/div[@class='u_menu_item']/a")))
        #             element.send_keys(Keys.ENTER)
        #             time.sleep(3)
        #             # 获取图片
        #             # element = spider.browser.findElements(By.XPATH('//div[@id="TANGRAM__PSP_10__QrcodeMain"]/img[@class="tang-pass-qrcode-img"]'))[0]
        #             element = WebDriverWait(spider.browser, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@id="TANGRAM__PSP_10__QrcodeMain"]/img[@class="tang-pass-qrcode-img"]')))
        #             print(element.get_attribute('src'))
        #         return HtmlResponse(url=spider.browser.current_url, encoding="utf-8",
        #                             body=spider.browser.page_source, status=200)
        #
        #     except Exception as e:
        #         print(f"chrome getting page error, Exception = {e}")
        #         return HtmlResponse(url=request.url, status=500, request=request)
        # else:
        #     # 页面爬取成功，构造一个成功的Response对象(HtmlResponse是它的子类)
        #     return HtmlResponse(url=request.url,
        #                         request=request,
        #                         status=200)

        return request

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
