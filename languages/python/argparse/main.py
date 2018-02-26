#!/usr/bin/env python
# coding: utf-8

import argparse

# Documentation https://docs.python.org/3/library/argparse.html

# Using example:
#    python main.py -h
#    python main.py file 5


def main(args):
    print(args)
    print("file1 = "+str(args.file1))
    print(" === End of this programme ===")    


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Demo program of argparse')

    parser.add_argument("file1" , help="Input file argument")
    parser.add_argument("value1", help="Integer argument", type=int)
    parser.add_argument("--file", help="A file")
    parser.add_argument("-f", "--config-file", 
        help="load personnal configuration file (defaut: settings.yaml)",
        metavar="CONF_FILE",
        default="settings.yaml")
    parser.add_argument("-a", "--activate", help="Boolean flag", action="store_true")
    parser.add_argument("-m", "--mode", type=int, choices=[0, 1, 2],
                    help="Select mode")


    group_vq = parser.add_mutually_exclusive_group()
    group_vq.add_argument("-v", "-vv", "--verbose", 
        help="enable verbosity: -v = INFO, -vv = DEBUG ", 
        action="count",
        default=0)
    group_vq.add_argument("-q", "--quiet", 
        help="quiet mode", 
        action="store_true")

    args = parser.parse_args()
    main(args)

