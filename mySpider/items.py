# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class BbsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=scrapy.Field()
    today=scrapy.Field()
    posting=scrapy.Field()
    member=scrapy.Field()
    vanfan_geyan=scrapy.Field()
    newmember=scrapy.Field()

class ScoreItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 姓名
    Name = scrapy.Field()
    # 学号
    Number = scrapy.Field()
    # 性别
    Sex=scrapy.Field()
    # 学院
    Depart=scrapy.Field()
    # 专业
    Majority=scrapy.Field()
    # 成绩
    Score=scrapy.Field()
    #照片地址
    image=scrapy.Field()
