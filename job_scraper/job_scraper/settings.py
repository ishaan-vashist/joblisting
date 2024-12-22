# Install SelectorReactor for compatibility with Windows
from twisted.internet import selectreactor
selectreactor.install()

BOT_NAME = "job_scraper"

SPIDER_MODULES = ["job_scraper.spiders"]
NEWSPIDER_MODULE = "job_scraper.spiders"

# Crawl responsibly by identifying yourself on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"

# Obey robots.txt rules (set to False to ensure scraping if necessary)
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 16

# Configure a delay for requests for the same website (default: 0)
DOWNLOAD_DELAY = 1  # Delay of 1 second between requests to avoid being blocked
RANDOMIZE_DOWNLOAD_DELAY = True  # Randomize delay to mimic human behavior

# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 8
CONCURRENT_REQUESTS_PER_IP = 8

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Override the default request headers to mimic a browser
DEFAULT_REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": USER_AGENT,
}

# Enable or disable downloader middlewares
DOWNLOADER_MIDDLEWARES = {
    "scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware": 810,
    "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": None,
}

# Enable or disable extensions
EXTENSIONS = {
    "scrapy.extensions.closespider.CloseSpider": 500,
}

# Enable and configure the AutoThrottle extension (enabled to be polite to the server)
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1  # Initial download delay
AUTOTHROTTLE_MAX_DELAY = 10  # Maximum download delay
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0  # Average number of requests Scrapy should send
AUTOTHROTTLE_DEBUG = False  # Enable this to debug AutoThrottle behavior

# Enable HTTP cache for development (disable in production)
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = "httpcache"
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Retry settings for handling failed requests
RETRY_ENABLED = True
RETRY_TIMES = 3  # Number of retries
RETRY_HTTP_CODES = [500, 502, 503, 504, 522, 524, 408, 429]  # Common retry status codes

# Logging
LOG_LEVEL = "INFO"

# Enable random User-Agent to mimic real users
FAKEUSERAGENT_PROVIDERS = [
    "scrapy_fake_useragent.providers.FakeUserAgentProvider",  # This will fetch random user-agent strings
    "scrapy_fake_useragent.providers.FakerProvider",
    "scrapy_fake_useragent.providers.FixedUserAgentProvider",
]

# Feed export settings
FEED_EXPORT_ENCODING = "utf-8"

# Close spider after scraping a certain number of items (optional)
CLOSESPIDER_ITEMCOUNT = 1000  # Adjust as per requirement

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
FEED_EXPORT_ENCODING = "utf-8"
