import scrapy
from mySpider.items import ScoreItem
import xlrd

class ScoreSpider(scrapy.Spider):
    name = "score"
    allowed_domains = ["202.194.40.116"]

    baseURL = "http://202.194.40.116:8080/pls/apex/f?p=101:1:2730495736949910::::P1_STUDENT_NO:"
    offset = 0

    start_urls = [baseURL + "201600800" + str(offset).zfill(3)]

    def parse(self, response):
        node_list = response.xpath('//*[@id="t20ContentMiddle"]')
        #//*[]
        for node in node_list:
            item = ScoreItem()
            if(node.xpath('//tr[1]/td[4]/text()').extract()):
                # 姓名 //*[@id="t20ContentMiddle"]/table[2]/tbody/tr[1]/td[4]
                item['Name'] = node.xpath('//tr[1]/td[4]/text()').extract()[0]
                #print(node.xpath('//tr[1]/td[2]/text()').extract()[0])

                # 学号
                item['Number'] = node.xpath('//tr[1]/td[2]/text()').extract()[0]

                # 性别
                item['Sex']=node.xpath('//tr[1]/td[6]/text()').extract()[0]

                # 学院//*[@id="t20ContentMiddle"]/table[2]/tbody/tr[2]/td[2]
                item['Depart']=node.xpath('//tr[2]/td[2]/text()').extract()[0]

                # 专业//*[@id="t20ContentMiddle"]/table[2]/tbody/tr[2]/td[4]
                item['Majority']=node.xpath('//tr[2]/td[4]/text()').extract()[0]

                # 成绩
                item['Score']=node.xpath('//tr[5]/td[6]/text()').extract()[0]

                # 照片
                item['image']=node.xpath('//tr[1]/td[7]/img/@src').extract()[0]

                yield item

        self.offset += 1
        url = self.baseURL + "201600800" + str(self.offset).zfill(3)
        yield scrapy.Request(url, callback=self.parse)  # callback函数可以更换，即可以使用不同的处理方法处理不同的页面


