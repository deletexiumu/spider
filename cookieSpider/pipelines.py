# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymysql import cursors
from twisted.enterprise import adbapi


class CookiespiderPipeline(object):

    @classmethod
    def from_settings(cls, settings):
        db_params = dict(
            host=settings['MYSQL_HOST'],
            user=settings['MYSQL_USER'],
            password=settings['MYSQL_PASSWD'],
            port=settings['MYSQL_PORT'],
            db=settings['MYSQL_DBNAME'],
            charset=settings['MYSQL_CHARSET'],
            use_unicode=True,
            cursorclass=cursors.Cursor
        )
        db_pool = adbapi.ConnectionPool('pymysql', **db_params)
        return cls(db_pool)

    def __init__(self, db_pool) -> None:
        self.db_pool = db_pool

    def process_item(self, item, spider):
        query = self.db_pool.runInteraction(self.insert_item, item)
        query.addErrback(self.handler_error, item, spider)
        return item

    def handler_error(self, failure, item, spider):
        print(failure)

    def insert_item(self, cursor, item):
        sql = "insert into jx3_trade_post(title, body_size, price, server, detail_url, photo) values (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (
        item['title'], item['body_size'], item['price'], item['server'], item['detail_url'], item['photo']))
