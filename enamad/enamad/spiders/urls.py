import scrapy
import csv

class Urls(scrapy.Spider) :
    name = "urls"
    index = 0
    def start_requests(self):
        page_url = []
        for i in range(2, 6668) :
            page_url.append(f"https://enamad.ir/DomainListForMIMT/Index/{i}")
        for url in page_url :
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        table = []
        # header = []
        # for i in range(1,9) :
        #     header += response.xpath(f"/html/body/div[1]/div[2]/div[2]/div/div/section/div/div/div/div/div/div[2]/ul/div/div/div[2]/div[1]/div[{i}]/text()").extract()
        # with open("url.csv","+a") as f :
        #     csvwriter = csv.writer(f)
        #     csvwriter.writerow(header)
        #     f.close()
        for i in range(1,31) :
            #add first col cause second col its an url and need change
            self.index+=1
            rows = [self.index]
            rows += ["".join(["https://www."]+response.xpath(f"/html/body/div[1]/div[2]/div[2]/div/div/section/div/div/div/div/div/div[2]/ul/div/div/div[2]/div[2]/div[2]/div[{i}]/div[2]/a[1]/text()").extract())]
            for j in range(3,9) :
                if j == 6 :
                    rows += [len(response.xpath(f"/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[{i}]/div[{j}]/text()").extract())-1]
                else :
                    rows += response.xpath(f"/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[{i}]/div[{j}]/text()").extract()
            table.append(rows)
        with open("url.csv","+a") as f :
            csvwriter = csv.writer(f)
            csvwriter.writerows(table)
            f.close()

        # with open("URLs.txt", "+a") as f :
        #     for url in all_urls :
        #         f.write("https://www."+url+"\n")
        #     f.close()
        print("yes")