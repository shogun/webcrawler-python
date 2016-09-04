from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from urlparse import urlparse, urljoin


class WiprodigitalSpider(CrawlSpider):
    name = "wiprodigital"
    allowed_domains = ['wiprodigital.com']
    start_urls = ['http://wiprodigital.com/']
    externalLinks = set()
    internalLinks = set()
    mediaLinks = set()

    rules = [Rule(LinkExtractor(allow=()), callback='parse_item', follow=True)]

    def parse_item(self, response):

        self.internalLinks.add(response.url)

        for sel in response.css('body a[href]'):
            url = sel.xpath('@href').extract()[0].split('#')[0]
            url = url.strip()
            parsed_url = urlparse(url)

            if parsed_url.hostname in self.allowed_domains:
                self.internalLinks.add(parsed_url.geturl())
            elif not url.startswith("mailto:"):
                if url:
                    self.externalLinks.add(url)

        for sel in response.css('body img'):
            url = urljoin(self.start_urls[0], sel.xpath('@src').extract()[0])
            if url:
                self.mediaLinks.add(url)
