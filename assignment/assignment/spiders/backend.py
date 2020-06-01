import scrapy
from ..items import AssignmentItem
from scrapy.http.request import Request


class medium(scrapy.Spider):
    name = 'articles'
    page_no = 2

    # allowed_domain = ['https://www.amazon.in/s?k=best+books&ref=nb_sb_noss_2']
    start_urls = [
        'https://www.flipkart.com/search?q=books&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
    ]

    # def make_requests_from_url(self, url):
    #  return Request(url, dont_filter=True, meta={
    #     'dont_redirect': True,
    #    'handle_httpstatus_list': [301, 302]
    # })

    def parse(self, response):
        items = AssignmentItem()

        quotes = response.css('._2cLu-l::text').extract()
        authors = response.css('._1rcHFq::text').extract()
        prices = response.css('._1Vfi6u ._1vC4OE::text').extract()
        ratings = response.css('.hGSR34::text').extract()

        #for item in zip(quotes, authors, prices, ratings):
        #     items = {
         #        'quotes': item[0],
          #       'authors': item[1],
           #      'prices': item[2],
            #     'ratings': item[3],
             #}
        items['quotes'] = quotes
        items['authors'] = authors
        items['prices'] = prices
        items['ratings'] = ratings

        yield items

        next_page = 'https://www.flipkart.com/search?q=books&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=' + str(medium.page_no)
        if medium.page_no <= 2:
            medium.page_no += 1
            yield response.follow(next_page, callback=self.parse)

