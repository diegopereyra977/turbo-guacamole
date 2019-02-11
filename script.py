#! /usr/bin/python

import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://listado.mercadolibre.com.uy/casa-en-venta-floresta#D[A:casa%20en%20venta%20floresta]']
    

    def parse(self, response):
        for next_item in response.css('li.results-item div > a'):
            yield response.follow(next_item, self.parse_childs)

        for next_page in response.css('a.andes-pagination__link'):
            yield response.follow(next_page, self.parse)


    
    def parse_childs(self, response):
        for title in response.css('.item-title'):
            yield {'TITULO >>>> ': title.css('.item-title__primary').get()}

