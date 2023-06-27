import requests

import logging
import logging.config

import time

from scraper import LOGGING_CONFIG, URL

from scraper.pages import Pages

logging.config.fileConfig(LOGGING_CONFIG)

logger = logging.getLogger('access')
dlogger = logging.getLogger('devel')

class App:

    _books = []

    def __init__(self):

        logger.info('Loading books list.')
        logger.info(f'Requesting {URL}')
        
        self.page_content = requests.get(URL).content

        dlogger.debug('Creating AllBooksPage from page content.')
        self.page = Pages(self.page_content)

        logger.info(f'Going through {self.page.page_count} pages of books...')

        self._books = self.books()

        self.books_generator = (x for x in self._books)


    def get_content(self):
        # return self.page_content
        return self.page.page_count

    def books(self):
        dlogger.debug(f'Finding all books')
        books = []

        for page_num in range(self.page.page_count):
            
            page_start = time.time()
            
            url = f'{URL}/catalogue/page-{page_num+1}.html'
            logger.info(f'Requesting {url}')

            page_content = requests.get(url).content
            logger.debug('Creating All Pages from page content.')
            
            page = Pages(page_content)
            # print(f'{url} took {time.time() - page_start}')
            
            books.extend(page.books)
        
        return books

    def next_book(self):
        return next(self.books_generator)

    def best_books(self):
        best_books = sorted(self._books, key=lambda x: x.rating * -1)[:5]
        return best_books

    def cheapest_books(self):
        cheapest_books = sorted(self._books, key=lambda x: x.price)[:5]
        return cheapest_books
