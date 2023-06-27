# __init__.py
from pathlib import Path

__app_name__ = "scrap"
__version__ = "0.1.0"


LOGGING_CONFIG = Path(__file__).parent / 'logging.conf'


USER_CHOICE = '''Enter one of the following

- 'b' to look at 5-star books
- 'c' to look at the cheapest books
- 'n' to just get the next available book on the page
- 'q' to exit

Enter your choice: '''

URL = 'http://books.toscrape.com'
# url = f'http://books.toscrape.com/catalogue/page-{page_num+1}.html'
    