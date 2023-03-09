import scrapy


class RedditbotSpider(scrapy.Spider):
    name = 'redditbot'
    allowed_domains = ['www.reddit.com/r/gameofthrones/']
    start_urls = ['http://www.reddit.com/r/gameofthrones/']

    def parse(self, response):
        #Extracting the content using css selectors
        titles = response.css('._eYtD2XCVieq6emjKBH3m::text').getall()
        times = response.css('span._2VF2J19pUIMSLJFky-7PEI::text').getall()
        comments = response.css('span.FHCV02u6Cp2zYL0fhQPsO::text').getall()
        for item in zip(titles,times,comments):
            yield {'title' : item[0],
                   'created_at' : item[1],
                   'comments' : item[2]}
        pass

    
    
    