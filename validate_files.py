#!/usr/bin/env python3
import os
import sys

from xml.etree import ElementTree as ET


def main(argv):
    for file in argv:
        path = os.path.abspath(file)
        if path.endswith(".html"):
            with open(path, "r") as f:
                # Parse HTML and check if the <img/> tag refers to a valid file
                index_html = f.read()
                root = ET.fromstring(index_html)
                img_src = root.find("img").attrib["src"]
                if os.path.exists(img_src) or os.path.exists(os.path.join(os.path.dirname(path), img_src)):
                    print(f"File in img tag exists: {img_src}")
                else:
                    raise Exception(f"File in img tag not found! {img_src}")
        elif file.endswith(".png"):
            with open(file, "rb") as f:
                magic_bytes = f.read(8)
                if magic_bytes == b"\x89PNG\r\n\x1a\n":
                    print(f"Ok PNG: {file}")
                else:
                    raise Exception(f"Bad png: {file}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        main(["index.html", "green.png"])
