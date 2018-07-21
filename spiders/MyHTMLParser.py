#!/usr/bin/env python
# -*- coding:utf-8 -*-


from HTMLParser import HTMLParser


class MyHTMLParser(HTMLParser):

    fr = {}
    count_index = 0
    fund_index = ["date", "org_rate", "private_rate", "inner_rate", "total_share"]

    def handle_data(self, data):
        if self.count_index < len(self.fund_index):
            self.fund_index[self.count_index] = data
        elif self.count_index < 2 * len(self.fund_index):
            self.fr[self.fund_index[self.count_index % 5]] = data

        self.count_index += 1
