# coding:utf-8
import scrapy
from scrapy import Request
# import traceback

from ..items import PostItem


class JX3PostSpider(scrapy.Spider):
    """
    JX3帖子爬虫类定义
    """
    name = 'JX3Post'
    allowed_domains = ['hongyuweids.com']
    start_urls = ['http://www.hongyuweids.com/pr.jsp?m22pageno=3']

    def parse(self, response):
        result_list = []
        # 获取产品列表
        product_list = response.xpath('//div[@class="productList"]').xpath('.//div[@class="productPicListForm "]')
        # 获取单条信息
        for product in product_list:
            result = PostItem()
            item_form = product.xpath('.//td[@class="propList    "]')
            # 读取数据
            value_element = item_form.xpath('.//div[@class="propDiv productName    "]/a/@title').extract()
            result['title'] = value_element[0] if value_element is not None and len(value_element)>0 else ''
            value_element = item_form.xpath('.//div[@class="propDiv productProp4    "]/span[@class="propValue"]/text()').extract()
            result['body_size'] = value_element[0] if value_element is not None and len(value_element)>0 else ''
            value_element = item_form.xpath('.//div[@class="propDiv productProp11    "]/span[@class="propValue g_stress mallPrice"]/text()').extract()
            result['price'] = value_element[0] if value_element is not None and len(value_element)>0 else ''
            value_element = item_form.xpath('.//div[@class="propDiv productProp6    "]/span[@class="propValue"]/text()').extract()
            result['server'] = value_element[0] if value_element is not None and len(value_element)>0 else ''
            value_element = item_form.xpath('.//div[@class="propDiv productName    "]/a/@href').extract()
            result['detail_url'] = 'http://www.hongyuweids.com/' + value_element[0] if value_element is not None and len(value_element)>0 else ''

            result_list.append(result)

        # 提交下层解析
        for result in result_list:
            if result['detail_url'] == '':
                result['photo'] = ''
                yield result
            else:
                yield Request(url=result['detail_url'], meta={"item_brief": result}, callback=self.get_photo_info)

        # 下一页请求
        next_page = response.xpath('//div[@id="pagenation22"]/div[@class="pagePrev"]')
        if next_page is not None:
            next_url = next_page.xpath('./a/@href').extract()[0]
            yield Request(url='http://hongyuweids.com'+next_url, callback=self.parse)

    def get_photo_info(self, response):
        """
        获取照片信息
        :param response:
        :return:
        """
        try:
            photo = response.xpath('//div[@class="richContent"]/p/img/@src').extract()[0]
            result = response.meta['item_brief']
            result['photo'] = "http:" + photo
        except:
            result = response.meta['item_brief']
            result['photo'] = ''

        yield result
