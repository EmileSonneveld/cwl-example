#!/usr/bin/env python3
import os
import sys

from xml.etree import ElementTree as ET


def main(argv):
    directory = argv[0]
    for file_name in os.listdir(directory):
        file = os.path.join(directory, file_name)
        if file.endswith(".html"):
            with open(file, "r") as f:
                # Parse HTML and check if the <img/> tag refers to a valid file
                index_html = f.read()
                root = ET.fromstring(index_html)
                img_src_relative = root.find("img").attrib["src"]
                img_src = os.path.join(directory, img_src_relative)
                if os.path.exists(img_src):
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
        else:
            raise Exception(f"Unknown file type: {file}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        # Replace with your tmp directory for testing:
        main(["/tmp/izpl4hgo/stgc3d7fe31-4962-4c43-a77d-2001c8e2c207/24wvoteh"])
