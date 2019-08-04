#!/usr/bin/env python3
import requests
from src.scraping import scraping_de
from src.utils import create_dir, save_file


def main():
    path = create_dir()
    url = "https://brasil.diplo.de/br-de/service/matriculaconsular/" \
          "2222228?fbclid=IwAR0MojqudTlgMKQjZG7nNqp9gr3-QSKyiiRdY0jeeBY336zm_3yqr_Oc_nc"

    content = scraping_de(url)

    for c in content:
        save_file(
            pathname=path,
            filename=c["file_name"],
            content=requests.get(c["xls_url"]).content
        )


if __name__ == '__main__':
    main()
