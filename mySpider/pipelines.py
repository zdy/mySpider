# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem;
import codecs
import os
import json
import time
from scrapy import signals
import mySpider.settings as settings
import pymysql
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
from mySpider.settings import IMAGES_STORE

class BbsPipeline(object):
    def __init__(self):
        self.file=codecs.open('data.json','w',encoding='utf-8')

    def process_item(self, item, spider):
        line=json.dumps(dict(item))+'\n'
        self.file.write(line.encode('utf-8').decode('utf-8'))
        return item

    def spider_closed(self,spider):
        self.file.close()

class ScorePipeline(object):
    # def __init__(self):
    #     self.f = open('shit.json','w')
    #
    # def process_item(self, item, spider):
    #     content = json.dumps(dict(item),ensure_ascii=False) + ',\n'
    #     self.f.write(content)
    #     return item
    #
    # def close_spider(self,spider):
    #     self.f.close()
    def process_item(self, item, spider):
        host = settings.MYSQL_HOST
        user = settings.MYSQL_USER
        psd = settings.MYSQL_PASSWORD
        db = settings.MYSQL_DB
        c = settings.CHARSET
        port = settings.MYSQL_PORT
        # 数据库连接
        con = pymysql.connect(host=host, user=user, passwd=psd, db=db, charset=c, port=port)
        # 数据库游标
        cue = con.cursor()
        print("mysql connect succes")  # 测试语句，这在程序执行时非常有效的理解程序是否执行到这一步
        # sql="insert into gamerank (rank,g_name,g_type,g_status,g_hot) values(%s,%s,%s,%s,%s)" % (item['rank'],item['game'],item['type'],item['status'],item['hot'])
        try:
            cue.execute("insert into score (Name,Number,Sex,Depart,Majority,Score,image) values(%s,%s,%s,%s,%s,%s,%s)",
                        [item['Name'], str(item['Number']), item['Sex'], item['Depart'], item['Majority'],item['Score'],item['image']])
            print("insert success")  # 测试语句
        except Exception as e:
            print('Insert error:', e)
            con.rollback()
        else:
            con.commit()
        con.close()
        return item


class PicPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        print('=======', request.__dict__)
        url = request.url
        # 防止有中文重名的特意加上时间鹾
        return '{0}-{1}.{2}'.format(request.meta['title'], str(time.time()).split('.')[0],'jpg')

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem('Image Downloaded Failed')
        return item

    def get_media_requests(self, item, info):
        # 从管道中获取图片的地址
        yield Request(url=item['image'], meta={'title': item['Number']})