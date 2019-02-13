#! /usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.firefox.options import Options

import time

import scrapy


driver = webdriver.Firefox()

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://listado.mercadolibre.com.uy/casa-en-venta-floresta#D[A:casa%20en%20venta%20floresta]']
    

    def parse(self, response):
        for next_item in response.css('li.results-item div > a'):
            yield response.follow(next_item, self.parse_childs)


        for next_page in response.css('a.andes-pagination__link'):
            yield response.follow(next_page, self.parse)


    
    def parse_childs(self, response):
        url = response.request.url

        driver.implicitly_wait(30)
        driver.get(url)
        driver.quit
    #    for title in response.css('.item-title'):
    #        yield {'price': title.css('.short-description__form').get()}

