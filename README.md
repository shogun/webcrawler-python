# Web crawler

## Task

 Web Crawler
Your task is to write a simple web crawler in a language of your choice.
The crawler should:

- be limited to one domain. Given a starting URL – say wiprodigital.com 
- it should visit all pages within the domain, but not follow the links to external sites such as Google or Twitter.

The output should be a simple site map, showing links to other pages under the same domain, links to static content such as images, and to external URLs.
We would like to see what you can produce in a couple of hours – please don’t spend much more than that. In addition, please

- ensure that what you do implement is production quality code
- briefly describe any tradeoffs you make through comments and / or in a README file
- include the steps needed to build and run your solution
   
Once done, please make your solution available on Github and forward the link with brief instruction on how to run it

## Description
This project is using **scrapy** internally to crawl pages.

Main tradeoffs:

- scrapy spider works on allowed domain list basis so this script is configured to crawl http://wiprodigital.com
- no package manger support yet

## Setup
    
    Requires scrapy to be installed: http://doc.scrapy.org/en/latest/intro/install.html
    
    $ git clone https://github.com/shogun/webcrawler-python.git
    $ cd webcrawler-python/

## Parameters

    $ python scrape.py -h
    usage: scrape.py [-h] [--log-level LOG_LEVEL] output_file
    
    Web Crawler.
    
    positional arguments:
      output_file           output file name
    
    optional arguments:
      -h, --help            show this help message and exit
      --log-level LOG_LEVEL
                            possible debug levels: CRITICAL, ERROR, WARNING, INFO,
                            DEBUG

## Usage

Run:

    $ python scrape.py sitemap.xml

## Example output XML file format

```xml
<?xml version="1.0" encoding="UTF-8"?>

<response>
    <internalLinks>
        <url>http://wiprodigital.com/</url>
        ...
    </internalLinks>
    <mediaLinks> 
        <url>http://17776-presscdn-0-6.pagely.netdna-cdn.com/wp-content/themes/wiprodigital/images/designit_logo.png</url>
        ...
    </mediaLinks>
    <externalLinks>
        <url>https://xebialabs.com/</url>
        ...
    </externalLinks>
</response>
```

## Example console log output

    $ python scrape.py sitemap.xml --log-level="DEBUG"
    2016-09-05 00:17:50 [scrapy] INFO: Scrapy 1.0.3 started (bot: scrapybot)
    2016-09-05 00:17:50 [scrapy] INFO: Optional features available: ssl, http11, boto
    2016-09-05 00:17:50 [scrapy] INFO: Overridden settings: {'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)', 'DOWNLOAD_DELAY': 0.25}
    2016-09-05 00:17:50 [scrapy] INFO: Enabled extensions: CloseSpider, TelnetConsole, LogStats, CoreStats, SpiderState
    2016-09-05 00:17:50 [scrapy] INFO: Enabled downloader middlewares: HttpAuthMiddleware, DownloadTimeoutMiddleware, UserAgentMiddleware, RetryMiddleware, DefaultHeadersMiddleware, MetaRefreshMiddleware, HttpCompressionMiddleware, RedirectMiddleware, CookiesMiddleware, ChunkedTransferMiddleware, DownloaderStats
    2016-09-05 00:17:50 [scrapy] INFO: Enabled spider middlewares: HttpErrorMiddleware, OffsiteMiddleware, RefererMiddleware, UrlLengthMiddleware, DepthMiddleware
    2016-09-05 00:17:50 [scrapy] INFO: Enabled item pipelines: 
    2016-09-05 00:17:50 [scrapy] INFO: Spider opened
    2016-09-05 00:17:50 [scrapy] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
    2016-09-05 00:17:50 [scrapy] DEBUG: Telnet console listening on 127.0.0.1:6023
    2016-09-05 00:17:51 [scrapy] DEBUG: Crawled (200) <GET http://wiprodigital.com/> (referer: None)
    2016-09-05 00:17:51 [scrapy] DEBUG: Filtered offsite request to 'www.facebook.com': <GET https://www.facebook.com/WiproDigital/>
    2016-09-05 00:17:51 [scrapy] DEBUG: Filtered offsite request to 'twitter.com': <GET https://twitter.com/wiprodigital>
    2016-09-05 00:17:51 [scrapy] DEBUG: Filtered offsite request to 'www.linkedin.com': <GET https://www.linkedin.com/company/wipro-digital>
    2016-09-05 00:17:51 [scrapy] DEBUG: Crawled (200) <GET http://wiprodigital.com/> (referer: http://wiprodigital.com/)
    2016-09-05 00:17:51 [scrapy] DEBUG: Filtered duplicate request: <GET http://wiprodigital.com/> - no more duplicates will be shown (see DUPEFILTER_DEBUG to show all duplicates)
    ...
    2016-09-05 00:18:40 [scrapy] DEBUG: Crawled (200) <GET http://wiprodigital.com/cases/in24/> (referer: http://wiprodigital.com/what-we-do/)
    2016-09-05 00:18:40 [scrapy] INFO: Closing spider (finished)
    2016-09-05 00:18:40 [scrapy] INFO: Dumping Scrapy stats:
    {'downloader/request_bytes': 56492,
    'downloader/request_count': 168,
    'downloader/request_method_count/GET': 168,
    'downloader/response_bytes': 950369,
    'downloader/response_count': 168,
    'downloader/response_status_count/200': 127,
    'downloader/response_status_count/301': 35,
    'downloader/response_status_count/404': 6,
    'dupefilter/filtered': 1494,
    'finish_reason': 'finished',
    'finish_time': datetime.datetime(2016, 9, 4, 23, 18, 40, 807277),
    'log_count/DEBUG': 251,
    'log_count/INFO': 7,
    'offsite/domains': 75,
    'offsite/filtered': 638,
    'request_depth_max': 8,
    'response_received_count': 133,
    'scheduler/dequeued': 168,
    'scheduler/dequeued/memory': 168,
    'scheduler/enqueued': 168,
    'scheduler/enqueued/memory': 168,
    'start_time': datetime.datetime(2016, 9, 4, 23, 17, 50, 522007)}
    2016-09-05 00:18:40 [scrapy] INFO: Spider closed (finished)

    
  