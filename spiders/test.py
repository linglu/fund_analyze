#!/usr/bin/env python
# -*- coding:utf-8 -*-


import requests  # $ pip install requests
import re
import json

# url = 'http://fund.eastmoney.com/f10/FundArchivesDatas.aspx?type=cyrjg&code=000738'
text = "截至2017-12-31，<a href='http://fund.eastmoney.com/000738.html'>中信建投货币A</a> 的基金机构持有0.01亿份，占总份额的6.78%，个人投资者持有0.12亿份，占总份额的93.22%"

# r = requests.get(url, stream=True)

allText = re.findall("<.+?>", text)
result = text.replace(allText[0], "").replace(allText[1], "")

print(result)

# result = re.search("{.+}", r.text)
# jsonstr = result.group().replace("content", "\"content\"").replace("summary", "\"summary\"")
# print(json.loads(jsonstr)['summary'])

