# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
class AssignmentPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("myproject.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS Table_tb""")
        self.curr.execute("""create table Table_tb(
                        quotes text,
                        authors text,
                        prices text, 
                        rankings text
                        )""")
    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item ):
        self.curr.execute("""insert into Table_tb values (?,?,?,?)""",(
            item['quotes'][0],
            item['authors'][0],
            item['prices'][0],
            item['ratings'][0]
        ))

        self.conn.commit()
