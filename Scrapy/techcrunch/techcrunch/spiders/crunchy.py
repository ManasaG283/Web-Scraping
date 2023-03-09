import scrapy


class CrunchySpider(scrapy.Spider):
    name = 'crunchy'
    allowed_domains = ['techcrunch.com/feed/']
    start_urls = ['http://techcrunch.com/feed/']

    def parse(self, response):
        #remove XML namespaces
        response.selector.remove_namespaces()
        titles = response.xpath("//item/title/text()").getall()
        authors = response.xpath("//item/creator/text()").getall()
        dates = response.xpath("//item/pubDate/text()").getall()
        links = response.xpath("//item/link/text()").getall()
        
        for item in zip(titles,authors,dates,links):
            yield {'title':item[0],
                   'author':item[1],
                   'date':item[2],
                   'link':item[3]
                  }
        pass