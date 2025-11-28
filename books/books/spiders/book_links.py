import scrapy

class Book_Links(scrapy.Spider) :
    name = "books"
    num = 1
    def start_requests(self):
        urls = []
        urls.append("https://books.toscrape.com/")
        for i in range(2,5) :
            urls.append(f"https://books.toscrape.com/catalogue/page-{i}.html")
        for url in urls :
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        titles = response.xpath("/html/body/div/div/div/div/section/div[2]/ol/li/article/h3/a/text()").extract()
        
        with open("title.txt", "+a") as f :
            f.write("\n")
            f.write(f"page {self.num}".center(70, "-"))
            f.write("\n")
            f.close()

        with open("title.txt", "+a") as f :
            for i in range(1, len(titles)+1) :
                f.write(f"{i} : {titles[i-1]}\n")
            f.close()
        self.num+=1