import scrapy


class ClubsItem(scrapy.Item):
    name = scrapy.Field()
    market_value = scrapy.Field()


class ClubsSpider(scrapy.Spider):
    name = 'clubs'
    allowed_domains = ['transfermarkt.com']
    start_urls = [
        'https://www.transfermarkt.com/premier-league/startseite/wettbewerb/GB1']

    def parse(self, response):
        club_rows = response.xpath("//*[@id = 'yw1']/table/tbody/tr")

        for row in club_rows:
            club_name = row.xpath('td[2]/a/text()').extract()[0]
            club_mv = row.xpath('td[7]/a/text()').extract()[0]

            yield ClubsItem({'name': club_name, 'market_value': club_mv})
