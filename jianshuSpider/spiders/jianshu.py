# -*- coding: utf-8 -*-
import scrapy
from jianshuSpider.items import MyspiderItem
from scrapy.selector import HtmlXPathSelector
from scrapy.utils.url import urljoin_rfc

class JianshuSpider(scrapy.Spider):
    name = 'jianshu'
    allowed_domains = ['www.jianshu.com']
    start_urls = ['http://www.jianshu.com/c/V2CqjW']

    # 获取IT专题的首页列表
    def parse(self, response):
        # print response.text
        hxs = HtmlXPathSelector(response)
        items = []
        url_list = hxs.xpath('//div[@class="content"]/a/@href').extract()
        # 先获取详情页链接列表，并存入item内
        for url in url_list:
            item = MyspiderItem()
            item['link'] = urljoin_rfc('http://www.jianshu.com', url)
            # print item['link']
            items.append(item)
        # 使用parse2作为回调方法,将item传入方法内
        for item in items:
            yield scrapy.Request(item["link"],meta={"item":item},callback=self.parse2)

    # 根据传入的item获取详情页数据
    def parse2(self,response):
        # print response.text
        hxs = HtmlXPathSelector(response)
        item = response.meta["item"]

        content_list = hxs.xpath('//div[@class="article"]')

        # 获取详情页数据,并使用yield将数据传给piplines
        for article in content_list:
            item["title"] = article.xpath('./h1/text()').extract()
            item["author"] = article.xpath('.//span[@class="name"]/a/text()').extract()
            item["article"] = article.xpath('.//div[@class="show-content"]//p/text()').extract()
            yield item
