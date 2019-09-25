from libgenapi import Libgenapi as lib
import re

lg = lib(["https://libgen.is", "http://gen.lib.rus.ec", "http://libgen.me"])


def download_books(lst) -> None:
    urls = []
    for book in lst:
        s = lg.search(book, "identifier")
        if s:
            urls.append(s[0]["mirrors"][0])
        else:
            print("ISBN#: {} was not found.".format(book))
    for url in urls:
        print("URL: {}".format(url))

    """
    Can't auto-download due to differences in mirror pages
    
    ans = input(
        "Found {} books. Would you like to download? [Y/n]".format(len(urls))).lower()
    while ans != 'n' and ans != 'y':
        ans = input('Please answer [Y/n]').lower()
    if ans == 'y':
        for i in range(len(urls)):
            print("Downloading ISBN#: {}...\n".format(lst[i]))
            wget.download(urls[i])
    else:
        print('Canceling...')"""
