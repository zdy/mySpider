from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy import log
from mySpider.items import BbsItem

class bbsSpider(Spider):
    name="bbs"
    allowed_domain=["bbs.uestc.edu.cn/"]
    start_urls=[
        "http://bbs.uestc.edu.cn/"
    ]
    def parse(self,response):
        sel=Selector(response)
        item=BbsItem()
        item['name']=sel.xpath('//title/text()').extract()
        item['today']=sel.xpath('/html/body/div[6]/div[4]/div[1]/p/em[1]/text()').extract()
        item['posting']=sel.xpath('/html/body/div[6]/div[4]/div[1]/p/em[3]/text()').extract()
        item['member']=sel.xpath('/html/body/div[6]/div[4]/div[1]/p/em[4]/text()').extract()
        item['vanfan_geyan']=sel.xpath('/html/body/div[6]/div[4]/div[1]/div/div/div[1]/a/span/text()').extract()
        item['newmember']=sel.xpath('/html/body/div[6]/div[4]/div[1]/p/em[5]/a/text()').extract()
        return item