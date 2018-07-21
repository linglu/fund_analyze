# -*- coding: utf-8 -*-
import scrapy
from FundsData.items import FundsdataItem
from scrapy.http import Request
import requests
import re
from FundsData.spiders.MyHTMLParser import MyHTMLParser
import json

class FundSpiderSpider(scrapy.Spider):
    name = 'fund_spider'
    allowed_domains = ['fund.eastmoney.com']
    start_urls = ['http://fund.eastmoney.com/trade/hb.html']

    def parse(self, response):

        itemlist = response.xpath('//tbody')

        for item in itemlist:

            fundlist = item.xpath('tr')

            for fund in fundlist:
                item = FundsdataItem()
                item['fund_code'] = fund.xpath('td/text()').extract()[0]
                item['fund_name'] = fund.xpath('td[@class="fname"]/a/text()').extract()[0]
                href = fund.xpath('td[@class="fname"]/a/@href').extract()[0]
                item['fund_earnings_perw'] = fund.css('td:nth-child(3) > span').xpath('text()').extract()[0]
                item['fund_earnings_seven'] = fund.css('td:nth-child(4)').xpath('text()').extract()[0]

                yield Request(href,
                              callback=self.content_callback,
                              meta={'item': item},
                              priority=10,
                              errback=self.error_back,
                              dont_filter=True
                              )

    def content_callback(self, response):

        item = response.meta['item']

        # 基金规模
        scale = response.css('.infoOfFund > table > tr > td:nth-child(2)').xpath('text()').extract()[0].strip()
        item['fund_scale'] = scale.replace("：", "")

        # 下载文件 http://fund.eastmoney.com/f10/FundArchivesDatas.aspx?type=cyrjg&code=000738&rt=0.3468087074675992
        # 并解析出需要的数据
        item['fund_private_prop'], item['fund_remark'] = self.parse_fund_archives(item['fund_code'])

        yield item

    def parse_fund_archives(self, code):

        url = 'http://fund.eastmoney.com/f10/FundArchivesDatas.aspx?type=cyrjg&code=' + code
        r = requests.get(url, stream=True)
        result = re.search("{.+}", r.text)
        jsonstr = result.group().replace("content", "\"content\"").replace("summary", "\"summary\"")
        text = json.loads(jsonstr)['summary']
        allText = re.findall("<.+?>", text)
        remark = text.replace(allText[0], "").replace(allText[1], "").replace("\n", "").strip()

        parser = MyHTMLParser()
        parser.feed(json.loads(jsonstr)['content'])
        return parser.fr['个人持有比例'], remark

    def error_back(self, e):
        print("报错了")
        pass
