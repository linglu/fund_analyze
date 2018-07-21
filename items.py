# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FundsdataItem(scrapy.Item):

    # 证券代码
    fund_code = scrapy.Field()

    # 证券名称
    fund_name = scrapy.Field()

    # 基金规模
    fund_scale = scrapy.Field()

    # 个人投资者比例
    fund_private_prop = scrapy.Field()

    # 万分收益
    fund_earnings_perw = scrapy.Field()

    # 七日年化
    fund_earnings_seven = scrapy.Field()

    # 备注
    fund_remark = scrapy.Field()

    pass
