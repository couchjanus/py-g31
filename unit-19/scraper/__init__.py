from pathlib import Path

__app_name__ = "scraper"
__version__ = "0.1.0"
URL = 'http://books.toscrape.com'

LOGGING_CONFIG = Path(__file__).parent / 'logging.conf'

USER_CHOICE = '''Enter one of the following

    - 'b' to look at 5-star books
    - 'c' to look at the cheapest books
    - 'n' to just get the next available book on the page
    - 'q' to exit

Enter your choice: '''
