from pathlib import Path
from bs4 import BeautifulSoup
import scrapy


class ExampleSpider(scrapy.Spider):
    name = "westelm"
    # allowed_domains = ["westelm.com"]
    # start_urls = ("https://www.westelm.com/products/solstice-coffee-table-h9127/?pkey=csolstice-collection",)

    def start_requests(self):
        urls = [
            "https://www.westelm.com/products/solstice-coffee-table-h9127/?pkey=csolstice-collection",
            # "https://quotes.toscrape.com/page/2/",
        ]
        for url in urls:
            request = scrapy.Request(url=url, callback=self.parse)
            yield request

    def parse(self, response):
        
        filename = f"westelm.html"
        Path(filename).write_bytes(response.body)
        soup = BeautifulSoup(response.text, "lxml")
        response.css("img").getall()
        self.log(f"Saved file {filename}")

    # def parse(self, response):
    #     # use lxml to get decent HTML parsing speed
    #     soup = BeautifulSoup(response.text, "lxml")
    #     # soup = BeautifulSoup(html_doc, 'html.parser')

    #     print(soup.prettify())
    #     # yield {"url": response.url, "title": soup.h1.string}
