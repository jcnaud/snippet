#!/usr/bin/env python
# coding: utf-8

from pyexcel_ods import get_data
import json


def main():
    data = get_data("file.ods")

    print(json.dumps(data))


if __name__ == '__main__':
    main()
