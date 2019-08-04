#!/usr/bin/env python3
import os
import errno


def create_dir():
    dirname = "../src/files/"
    pathname = os.path.expanduser(f"{dirname}")

    if not os.path.exists(pathname):
        try:
            os.makedirs(pathname)
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
    return pathname


def save_file(pathname, filename, content):
    with open(f"{pathname}{filename}", "wb") as f:
        f.write(content)
        print(f"Download file: {pathname}{filename}")
