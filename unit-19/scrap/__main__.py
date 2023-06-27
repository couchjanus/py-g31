""" Scrap entry point script. scrap/__main__.py"""

import logging
import logging.config

from scrap import __app_name__, USER_CHOICE, LOGGING_CONFIG

from scrap.app import App

# create logger
logging.config.fileConfig(LOGGING_CONFIG)

logger = logging.getLogger('devel')

def print_best_books(app):
    logger.debug('Finding best books by rating...')
    # print(app.get_content())
    # print(app.books())

    for book in app.best_books():
        print(book)

def print_cheapest_books(app):
    logger.debug('Finding best books by price...')

    for book in app.cheapest_books():
        print(book)

def get_next_book(app):
    logger.debug('Getting next book from generator of all books...')
    print(app.next_book())

user_choices = {
    'b': print_best_books,
    'c': print_cheapest_books,
    'n': get_next_book
}

def main():
    """This is entry point function. """

    user_input = input(USER_CHOICE)

    book_app = App()

    while user_input != 'q':
        logger.debug('User did not choose to exit program.')
        if user_input in ('b', 'c', 'n'):
            user_choices[user_input](book_app)
        else:
            print('Please choose a valid command.')
    user_input = input(USER_CHOICE)
    
logger.debug('Terminating program...')

if __name__ == "__main__":
    main()
