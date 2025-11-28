import scrapy

class Info(scrapy.Spider) :
    name = "info"

    def start_requests(self):
        with open("url.csv","r") as f :
            f.close()
        return None