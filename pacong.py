from lxml import etree
import requests
url = "https://maoyan.com/board"
# proxies={'http':'http://39.108.170.173:80'}
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
response = requests.get(url,headers=headers).text
# print(response)
tree = etree.HTML(response)
dd_list=tree.xpath('//dd')

for dd in dd_list:
    movie =dd.xpath('.//p[@class="name"]/a[last()]/text()')