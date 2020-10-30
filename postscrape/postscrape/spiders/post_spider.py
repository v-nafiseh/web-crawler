import scrapy
import csv

class Scraper(scrapy.Spider):

    name = 'spider'
    start_urls = ["https://bagheketab.com"]

    csv_file = open('my_csv_image_urls_2','w')
    csv_writer = csv.writer(csv_file)

    def parse(self, response):
        item = PostscrapeItem()
        item['image_urls'] = []

        all = response.css('img').xpath('@src').extract()

        for url in all:
            if not str(url).startswith(('http','https')):
                item['image_urls'].append(response.urljoin(url))
            item['image_urls'].append(url) 

        for it in item['image_urls']:
            Scraper.csv_writer.writerow([it])

        Scraper.csv_file.close()    

class PostscrapeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    images = scrapy.Field()
    image_urls = scrapy.Field() 
