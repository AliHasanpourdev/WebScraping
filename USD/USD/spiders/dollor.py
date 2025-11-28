import scrapy

class Usd_Price(scrapy.Spider) :
    name = "usd"

    def start_requests(self):
        urls = []

        for url in urls :
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        return None