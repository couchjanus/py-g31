# pages.py
import re
import logging
import logging.config

from bs4 import BeautifulSoup

from scrap import LOGGING_CONFIG

from scrap.locators.page_locators import PageLocators

from scrap.parsers.book import BookParser


logging.config.fileConfig(LOGGING_CONFIG)
logger = logging.getLogger('access')
dlogger = logging.getLogger('devel')

class Pages:
    def __init__(self, page):
        # dlogger.debug('Parsing page content with BeautifulSoup HTML parser.')
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        # dlogger.debug(f'Finding all books in the page using `{PageLocators.BOOKS}`')
        return [BookParser(e) for e in self.soup.select(PageLocators.BOOKS)]

    @property
    def page_count(self):
        # dlogger.debug('Finding all number of catalogue pages available...')
        content = self.soup.select_one(PageLocators.PAGER).string
        logger.info(f'Found number of catalogue pages available: {content}'.encode('utf-8'))
        pattern = 'Page [0-9]+ of ([0-9]+)'
        matcher = re.search(pattern, content)
        pages = int(matcher.group(1))
        # logger.info(f'Extracted number of pages as integer: `{pages}`.')
        return pages

