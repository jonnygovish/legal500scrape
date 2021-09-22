# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FirmscrapeItem(scrapy.Item):
    
    Company = scrapy.Field()
    City = scrapy.Field()
    Address = scrapy.Field()
    Website = scrapy.Field()
    Phone_number = scrapy.Field()
    Email_address = scrapy.Field()
    Practice_heads = scrapy.Field()
    Key_clients = scrapy.Field()
    Membership = scrapy.Field()
    Lawyer_list = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()

    
