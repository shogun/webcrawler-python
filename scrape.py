from lxml import etree
from crawler import Crawler
import argparse

parser = argparse.ArgumentParser(description='Web Crawler.')
parser.add_argument('output_file', help='output file name')
parser.add_argument('--log-level', help='possible debug levels: CRITICAL, ERROR, WARNING, INFO, DEBUG')

args = parser.parse_args()

log_level = 'INFO'
if args.log_level:
    log_level = args.log_level

crawler = Crawler(log_level)

xml = crawler.crawl()
if len(xml):
    output = '<?xml version="1.0" encoding="UTF-8"?>' + "\n\n"
    output += etree.tostring(xml, pretty_print=True)

    with open(args.output_file, 'w') as f:
        f.write(output)

