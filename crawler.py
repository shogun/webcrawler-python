from scrapy.crawler import CrawlerProcess

from wiprodigital_spider import WiprodigitalSpider
from lxml import etree


class Crawler:

    def __init__(self, log_level='INFO'):
        self.logLevel = log_level

    def crawl(self, ):

        spider = WiprodigitalSpider()

        process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
            'DOWNLOAD_DELAY': 0.25,
            'LOG_LEVEL': self.logLevel,
            'DOWNLOAD_HANDLERS': {'s3': None}  # hack
        })

        process.crawl(spider)
        process.start()

        return self.get_xml_output(spider)

    def get_xml_output(self, spider):
        """
        :type spider: WiprodigitalSpider
        """
        root = etree.Element('response')

        internal_links = etree.Element('internalLinks')
        for link in spider.internalLinks:
            internal_links.append(self.build_xml_row_element(link))
        root.append(internal_links)

        media_links = etree.Element('mediaLinks')
        for link in spider.mediaLinks:
            media_links.append(self.build_xml_row_element(link))
        root.append(media_links)

        external_links = etree.Element('externalLinks')
        for link in spider.externalLinks:
            external_links.append(self.build_xml_row_element(link))
        root.append(external_links)

        return root

    def build_xml_row_element(self, link):
        url = etree.Element('url')
        url.text = link
        return url
