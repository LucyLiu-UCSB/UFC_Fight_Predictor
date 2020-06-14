import scrapy
import string


class figherSpider(scrapy.Spider):

    name = 'fighters'

    def start_requests(self):
        start_urls = ['http://www.ufcstats.com/statistics/fighters?char=' + char + '&page=all' for char in string.ascii_lowercase]

        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # get the fighter links
        links = response.css('tr.b-statistics__table-row td.b-statistics__table-col a::attr(href)').extract()
        for link in links:
            yield scrapy.Request(link, callback=self.parse_fighter)

    def parse_fighter(self, response):
        yield {
            'name': response.xpath('/html/body/section/div/h2/span[1]/text()').get().strip(),
            'height':  response.css('li.b-list__box-list-item.b-list__box-list-item_type_block::text')[1].get().strip(),
            'reach': response.css('li.b-list__box-list-item.b-list__box-list-item_type_block::text')[5].get().strip(),
            'date_birth': response.css('li.b-list__box-list-item.b-list__box-list-item_type_block::text')[9].get().strip()
        }




