import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from imdb.items import ImdbItem

class ImdbSpider(scrapy.Spider):
    name = "imdb"
    allowed_domains = ["imdb.com"]
    rules = (
        Rule(LinkExtractor(restrict_xpaths=('//*[@id="main"]/div/div[4]/a')),
            process_links=lambda links: filter(lambda l: 'Next' in l.text, links),
            callback='parse',
            follow=True),
    )

    def start_requests(self):
        start_url = "http://www.imdb.com/search/title?year=2014,2014&title_type=feature&sort=moviemeter,asc"
        yield scrapy.Request(start_url)


    def parse(self, response):
        print ("parse page !!!!!!!!!!!!!!")
        print("check the length -------------" + str(len(response.xpath("//*[@id='main']/div/div[3]/div"))))
        for movie in response.xpath("//*[@id='main']/div/div[3]/div"):
            item = ImdbItem()
            item['Title'] = movie.xpath('div[1]/div[3]/h3/a/text()').extract()[0]
            print("title ---------------- " + item['Title'])
        # make sure that the dynamically generated start_urls are parsed as well

    parse_start_url = parse

    def parseMovieDetails(self, response):
        pass
