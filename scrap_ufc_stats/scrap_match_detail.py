import scrapy

class matchSpider(scrapy.Spider):
    name = 'matches'

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
        # get matches links on the same date
        links = response.css('tr::attr(data-link)').extract()
        for link in links:
            yield scrapy.Request(link, callback=self.parse_each_match)

    def parse_each_match(self, response):
        # get the single match data
        fighter_data1 = response.css('div.b-fight-details__person')[0]
        fighter_data2 = response.css('div.b-fight-details__person')[1]

        yield {
            'fight_name': response.css('h2.b-content__title a::text').get().strip(),
            'method': response.css('i.b-fight-details__text-item_first i::text')[1].get(),
            'round': response.css('i.b-fight-details__text-item::text')[1].get().strip(),
            'time': response.css('i.b-fight-details__text-item::text')[3].get().strip(),

            'fighter_1': fighter_data1.css('a::text').get().strip(),
            'fighter_1_result': fighter_data1.css('i::text').get().strip(),

            'fighter_2': fighter_data2.css('a::text').get().strip(),
            'fighter_2_result': fighter_data2.css('i::text').get().strip(),

            'KD_1': response.xpath(
                '//html/body/section/div/div/section[2]/table/tbody/tr/td[2]/p[1]/text()').get().strip(),
            'KD_2': response.xpath(
                '//html/body/section/div/div/section[2]/table/tbody/tr/td[2]/p[2]/text()').get().strip(),
            'sig_str_1': response.xpath(
                '//html/body/section/div/div/section[2]/table/tbody/tr/td[3]/p[1]/text()').get().strip(),
            'sig_str_2': response.xpath(
                '//html/body/section/div/div/section[2]/table/tbody/tr/td[3]/p[2]/text()').get().strip(),
            'sig_str_pct_1': response.xpath(
                '//html/body/section/div/div/section[2]/table/tbody/tr/td[4]/p[1]/text()').get().strip(),
            'sig_str_pct_2': response.xpath(
                '//html/body/section/div/div/section[2]/table/tbody/tr/td[4]/p[2]/text()').get().strip(),
            'total_str_1': response.xpath(
                '//html/body/section/div/div/section[2]/table/tbody/tr/td[5]/p[1]/text()').get().strip(),
            'total_str_2': response.xpath(
                '//html/body/section/div/div/section[2]/table/tbody/tr/td[5]/p[2]/text()').get().strip(),
            'td_1': response.xpath(
                '//html/body/section/div/div/section[2]/table/tbody/tr/td[6]/p[1]/text()').get().strip(),
            'td_2': response.xpath(
                '//html/body/section/div/div/section[2]/table/tbody/tr/td[6]/p[2]/text()').get().strip(),
            'td_pct_1': response.xpath(
                '//html/body/section/div/div/section[2]/table/tbody/tr/td[7]/p[1]/text()').get().strip(),
            'td_pct_2': response.xpath(
                '//html/body/section/div/div/section[2]/table/tbody/tr/td[7]/p[2]/text()').get().strip(),
            'sub_att_1': response.xpath(
                '//html/body/section/div/div/section[2]/table/tbody/tr/td[8]/p[1]/text()').get().strip(),
            'sub_att_2': response.xpath(
                '//html/body/section/div/div/section[2]/table/tbody/tr/td[8]/p[2]/text()').get().strip(),
            'pass_1': response.xpath(
                '//html/body/section/div/div/section[2]/table/tbody/tr/td[9]/p[1]/text()').get().strip(),
            'pass_2': response.xpath(
                '//html/body/section/div/div/section[2]/table/tbody/tr/td[9]/p[2]/text()').get().strip(),
            'head_1': response.xpath(
                '//html/body/section/div/div/table/tbody/tr/td[4]/p[1]/text()').get().strip(),
            'head_2': response.xpath(
                '//html/body/section/div/div/table/tbody/tr/td[4]/p[2]/text()').get().strip(),
            'body_1': response.xpath(
                '//html/body/section/div/div/table/tbody/tr/td[5]/p[1]/text()').get().strip(),
            'body_2': response.xpath(
                '//html/body/section/div/div/table/tbody/tr/td[5]/p[2]/text()').get().strip(),
            'leg_1': response.xpath(
                '//html/body/section/div/div/table/tbody/tr/td[6]/p[1]/text()').get().strip(),
            'leg_2': response.xpath(
                '//html/body/section/div/div/table/tbody/tr/td[6]/p[2]/text()').get().strip(),
            'distance_1': response.xpath(
                '//html/body/section/div/div/table/tbody/tr/td[7]/p[1]/text()').get().strip(),
            'distance_2': response.xpath(
                '//html/body/section/div/div/table/tbody/tr/td[7]/p[2]/text()').get().strip(),
            'clinch_1': response.xpath(
                '//html/body/section/div/div/table/tbody/tr/td[8]/p[1]/text()').get().strip(),
            'clinch_2': response.xpath(
                '//html/body/section/div/div/table/tbody/tr/td[8]/p[2]/text()').get().strip(),
            'ground_1': response.xpath(
                '//html/body/section/div/div/table/tbody/tr/td[9]/p[1]/text()').get().strip(),
            'ground_2': response.xpath(
                '//html/body/section/div/div/table/tbody/tr/td[9]/p[2]/text()').get().strip()

        }








