# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql


class FundsdataPipeline(object):

    connection = ''

    def process_item(self, item, spider):

        cur = self.connection.cursor()
        try:

            fund_name = item['fund_name']
            fund_code = item['fund_code']
            fund_scale = item['fund_scale']
            fund_private_prop = item['fund_private_prop']
            fund_earnings_perw = item['fund_earnings_perw']
            fund_earnings_seven = item['fund_earnings_seven']
            fund_remark = item['fund_remark']

            sql = "INSERT INTO `fund_hb` (" \
                  "`fund_name`, " \
                  "`fund_code`, " \
                  "`fund_scale`, " \
                  "`fund_private_prop`, " \
                  "`fund_earnings_perw`, " \
                  "`fund_earnings_seven`, " \
                  "`fund_remark`) VALUES (%s, %s, %s, %s, %s, %s, %s)"

            cur.execute(sql, (fund_name, fund_code, fund_scale, fund_private_prop, fund_earnings_perw, fund_earnings_seven, fund_remark))

        except Exception as e:
            print('Insert error:', e)
            self.connection.rollback()
        else:
            self.connection.commit()

        return item

    def open_spider(self, spider):

        # Connect to the database
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='liangjiu2009',
            db='fund',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor)

        pass

    def close_spider(self, spider):
        self.connection.close()
        pass
