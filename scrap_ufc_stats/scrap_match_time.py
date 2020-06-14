import scrapy

class matchTimeSpider(scrapy.Spider):
    name = 'match_time'

    def start_requests(self):
        start_urls = [
            'http://ufcstats.com/statistics/events/completed?page=all'
        ]

        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # get the match event links
        links = response.css('td.b-statistics__table-col i.b-statistics__table-content a::attr(href)').extract()
        for link in links:
            yield scrapy.Request(link, callback=self.parse_matches)

    def parse_matches(self, response):
        yield {
            'fight_name': response.css('span.b-content__title-highlight::text').get().strip(),
            'fight_date': response.css('li.b-list__box-list-item::text')[1].get().strip() # the fight date
        }
