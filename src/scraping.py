#!/usr/bin/env python3
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup


def scraping_de(url):
    index_page = '/'.join(url.split('/')[0:3])

    with urlopen(url) as u:
        soup = BeautifulSoup(u, "html5lib")

    xls_hrefs = soup.find_all("a", href=re.compile("xls"))
    xls_file_name = [f"{t.get('title').lower().replace(' ', '_')}.xlsx" for t in xls_hrefs]
    xls_ = [f"{index_page}{h.get('href')}" for h in xls_hrefs]

    xls_content = []

    for r in range(0, len(xls_file_name)):
        xls_dic = {
            "file_name": xls_file_name[r],
            "xls_url": xls_[r]
        }
        xls_content.append(xls_dic)

    return xls_content
