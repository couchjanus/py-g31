import logging
import logging.config

from scraper import LOGGING_CONFIG, __app_name__, USER_CHOICE
from scraper.app import App

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
    user_input = input(USER_CHOICE)
    
    app_inst = App()
    
    while user_input != 'q':
        logger.debug('User did not choose to exit programm.')
        
        if user_input in ('b', 'c', 'n'):
            user_choices[user_input](app_inst)
            # break
        else:
            print("Please choose a valid command.")
            
        user_input = input(USER_CHOICE)
    
    logger.debug('Terminating programm.')
        
if __name__ == "__main__":
    main()
