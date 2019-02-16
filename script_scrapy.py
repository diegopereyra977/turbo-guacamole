#! /usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options

from bs4 import BeautifulSoup

import scrapy
import time
import sys
import pdb
import csv


driver = webdriver.Firefox()
lista = [] 

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://listado.mercadolibre.com.uy/casa-en-venta-floresta#D[A:casa%20en%20venta%20floresta]']
    

    def parse(self, response):
        for next_item in response.css('li.results-item div > a'):
            yield response.follow(next_item, self.parse_childs)
            break

        for next_page in response.css('a.andes-pagination__link'):
            yield response.follow(next_page, self.parse)
            
        with open('casas_floresta.csv', 'w') as casas_floresta_csv:
            fieldnames= ['ml_id','title','direccion', 'precio', 'descripcion','specs_list']

            writer = csv.DictWriter(casas_floresta_csv, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            writer.writerows(lista)

            casas_floresta_csv.close()
 

    
    def parse_childs(self, response):
        url = response.request.url
        driver.implicitly_wait(30)
        driver.get(url)
        html = driver.page_source
        soap = BeautifulSoup(html)
        obj={ 
                "ml_id":soap.select_one('input[name="item_id"]').get('value'), 
                "title":soap.title.text,
                "direccion":soap.select_one(".item-title__primary").text,
                "precio":soap.select_one(".price-tag-fraction").text,
                "descripcion":soap.select_one("div.item-description__text").text,
                "specs_list":soap.select_one("ul.specs-list").text,

                }
        lista.append(obj)
        print(lista)

        driver.quit

    #    for title in response.css('.item-title'):
    #        yield {'price': title.css('.short-description__form').get()}

