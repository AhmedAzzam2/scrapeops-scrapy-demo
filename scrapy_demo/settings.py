import datetime

BOT_NAME = 'scrapy_demo'

SPIDER_MODULES = ['scrapy_demo.spiders']
NEWSPIDER_MODULE = 'scrapy_demo.spiders'

# Add Your ScrapeOps API Key
SCRAPEOPS_API_KEY = 'YOUR_API_KEY'

# Add In The ScrapeOps Extension
EXTENSIONS = {
        'scrapeops_scrapy.extension.ScrapeOpsMonitor': 500, 
        }

# Update The Download Middlewares
DOWNLOADER_MIDDLEWARES = {
'scrapeops_scrapy.middleware.retry.RetryMiddleware': 550,
'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
}

# Add FEED_URI setting
FEED_FORMAT = 'csv'
the_argument = getattr(settings, 'the_argument', None)
FEED_URI = 'output/{}_{}.csv'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), the_argument) if the_argument else 'output/{}.csv'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


