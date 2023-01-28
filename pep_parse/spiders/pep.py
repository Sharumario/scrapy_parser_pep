import re
import scrapy

from ..items import PepParseItem
from ..settings import PEPS_DOMAIN, URL


PATERN_NUMBER_NAME = r'\w*\W*(?P<number>\d+)\W+(?P<name>.+)'


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [PEPS_DOMAIN]
    start_urls = [URL.format(url=PEPS_DOMAIN)]

    def parse(self, response):
        for pep_link in response.css('#numerical-index tbody tr'):
            yield response.follow(
                pep_link.css('a::attr(href)').get(), callback=self.parse_pep)

    def parse_pep(self, response):
        number, name = re.search(
            PATERN_NUMBER_NAME,
            response.css("#pep-content h1 ::text").get(),
        ).groups()
        data = {
            'number': number,
            'name': name,
            'status': response.css(
                'dt:contains("Status") + dd abbr::text'
            ).get()
        }
        yield PepParseItem(data)
