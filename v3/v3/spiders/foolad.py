import scrapy
import json


class FooladSpider(scrapy.Spider):
    name = "foolad"
    allowed_domains = ["web-api.varzesh3.com"]
    start_urls = ["https://web-api.varzesh3.com"]
    for i in range(38) :
        start_urls.append("https://web-api.varzesh3.com/v2.0/football/teams/9/results?skip="+str(1+24*i))

    def start_requests(self) :
        for url in self.start_urls :
            yield scrapy.Request(url=url, callback=self.parse)
        
    def parse(self, response) :
        data = json.loads(response.text)
        for item in data["items"] :
            yield {
                "تاریخ" : item["date"],
                "ساعت" : item["time"],
                "مسابقات" : item["league"]["name"],
                "فصل" : item["league"]["season"],
                "عنوان" : str(item["title"]).replace(" هفته", "") if "هفته" in str(item["title"]) else item["title"],
                "حریف" : item["guest"]["name"] if item["host"]["name"]=="فولاد" else item["host"]["name"],
                "گل زده" : item["goals"]["guest"] if item["guest"]["name"]=="فولاد" else item["goals"]["host"],
                "گل خورده" : item["goals"]["host"] if item["guest"]["name"]=="فولاد" else item["goals"]["guest"],
                "تفاضل گل" : item["goals"]["guest"]-item["goals"]["host"] if item["guest"]["name"]=="فولاد" else item["goals"]["host"]-item["goals"]["guest"],
                "امتیاز" : 3 if (item["goals"]["guest"]-item["goals"]["host"]>0 and item["guest"]["name"]=="فولاد") or (item["goals"]["host"]-item["goals"]["guest"]>0 and item["host"]["name"]=="فولاد") else 1 if item["goals"]["guest"]==item["goals"]["host"] else 0, 
                "بازی در خانه" : 1 if item["host"]["name"]=="فولاد" else 0, 
                "لینک بازی" : item["video"]["link"] if "video" in item else None
            }
