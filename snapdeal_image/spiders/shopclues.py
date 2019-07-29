# -*- coding: utf-8 -*-
import scrapy


class ShopcluesSpider(scrapy.Spider):
    name = 'shopclues'
    allowed_domains = ['www.shopclues.com']
    start_urls = ['http://www.shopclues.com/mobiles-smartphones.html?facet_network_type[]=4G&fsrc=facet_network_type']
    #location of csv file
    custom_settings = {
       'FEED_URI' : 'tmp/shopclues.csv'
    }
    def parse(self, response):
        #Extract product information
        titles = response.css('img::attr(title)').extract()
        images = response.css('img::attr(data-img)').extract()
        prices = response.css('.p_price::text').extract()
        discounts = response.css('.prd_discount::text').extract()


        for item in zip(titles,prices,images,discounts):
            scraped_info = {
               'title' : item[0],
               'price' : item[1],
               'image_urls' : item[2], #Set's the url for scrapy to download images
               'discount' : item[3]
           }

            yield scraped_info