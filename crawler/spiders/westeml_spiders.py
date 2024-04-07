import json
from pathlib import Path
from bs4 import BeautifulSoup
import scrapy


class WestelmSpider(scrapy.Spider):
    name = "westelm"
    # allowed_domains = ["westelm.com"]
    # start_urls = ("https://www.westelm.com/products/solstice-coffee-table-h9127/?pkey=csolstice-collection",)

    def start_requests(self):
        urls = [
            "https://www.westelm.com/products/solstice-coffee-table-h9127/?pkey=csolstice-collection",
            "https://www.westelm.com/products/wanderer-shag-rug-t5939/?pkey=cbedroom-rugs"
        ]
        for url in urls:
            request = scrapy.Request(url=url, callback=self.parse)
            yield request

    def parse(self, response):
        print("response is type ",type(response))
        # response.css("a::attr(href)")[10]  # get all links
        img: scrapy.Selector
        for img in response.css("img"):
            entry = {
                "product": img.xpath("@alt").get(),
                "data-src": img.xpath("@data-src").getall(),
            }
            append_json("westelm2.jsonl", entry)

        # next_page = response.css("li.next a::attr(href)").get()
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)  # crawl to next page
        

def append_json(filepath: str, entry: dict):
    with open(filepath, mode='a', encoding='utf-8') as feedsjson:
        json.dump(entry, feedsjson)