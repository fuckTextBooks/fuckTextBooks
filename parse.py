from bs4 import BeautifulSoup as bs
import re
import time


def parse(html):
    # Use bs4 to parse list of ISBNS from image URL
    isbn_lst = []
    soup = bs(html, 'html.parser')
    td_tags = soup.find_all(name='td', class_='book-cover')
    for td in td_tags:
        img = td.find('img')
        pattern = re.compile("(?:cover_image.asp\?Key=)([0-9]{10})")
        isbn = re.match(pattern, img['src'])
        if isbn:
            # Adds isbn to list of isbns (isbn_lst)
            isbn_lst.append(isbn.group(1))

    return isbn_lst
