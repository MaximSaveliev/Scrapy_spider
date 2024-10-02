# Scrapy settings for scrapyspider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "scrapyspider"

SPIDER_MODULES = ["scrapyspider.spiders"]
NEWSPIDER_MODULE = "scrapyspider.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "scrapyspider (+http://www.yourdomain.com)"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "scrapyspider.middlewares.ScrapyspiderSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "scrapyspider.middlewares.ScrapyspiderDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "scrapyspider.pipelines.ScrapyspiderPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 1
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 10
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"


# PROXY_LIST = [
#     "https://40.84.24.155:80",
#     "https://173.0.255.16:45554",
#     "https://199.19.95.247:1080",
#     "https://199.19.95.130:1080",
#     "https://216.39.173.51:9001",
#     "https://91.121.42.68:80",
#     "https://66.253.164.20:45554",
#     "https://69.36.65.214:1080",
#     "https://172.87.9.218:45554",
#     "https://173.0.254.238:45554",
#     "https://174.141.207.88:45554",
#     "https://162.219.230.119:45554",
#     "https://216.8.217.243:45554",
#     "https://216.171.17.119:45554",
#     "https://104.145.70.226:45554",
#     "https://54.202.219.193:80",
#     "https://207.177.47.42:45554",
#     "https://76.191.26.232:45554",
#     "https://216.171.16.123:45554",
#     "https://76.10.41.124:45554",
#     "https://75.103.143.93:45554",
#     "https://68.39.112.128:13479",
#     "https://173.245.150.34:45554",
#     "https://76.191.26.65:45554",
#     "https://76.10.43.164:45554",
#     "https://104.145.103.38:45554",
#     "https://24.219.71.59:45554",
#     "https://68.180.3.212:45554",
#     "https://178.213.145.24:8080",
#     "https://12.35.68.239:45554"
# ]

# DOWNLOADER_MIDDLEWARES = {
#     'scrapyspider.middlewares.ProxyMiddleware': 543,
# }
