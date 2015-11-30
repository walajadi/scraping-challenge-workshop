# -*- coding: utf-8 -*-

from scrapy import Spider, Request
from ..items import PersonItem


class MyScraper(Spider):
    name = u'myscraper'


    def start_requests(self):
        # First request
        yield Request(
            url=u'https://scraping-challenge.herokuapp.com/onepage',
            callback=self.parse,
        )


    def parse(self, response):
        # Find a list of div which contains a person (use CSS)
        persons_el = response.css('.person')

        # Browse the list
        for person_el in persons_el:

            # Create a new item
            item = PersonItem()

            # Extract the name of the person (use CSS + XPath)
            name_el = person_el.css('.name').xpath('text()').extract()
            if len(name_el) > 0:
                item['name'] = name_el[0]

            # Extract the ticket fare of the person (use CSS + XPath)
            ticket_fare_el = person_el.css('.ticket_fare').xpath('text()').extract()
            if len(ticket_fare_el) > 0:
                item['ticket_fare'] = ticket_fare_el[0]

            # Export the item
            yield item
