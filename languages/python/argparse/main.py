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
    parser.add_argument("-a", "--activate", help="Boolean flag", action="store_true")
    parser.add_argument("-v","-vv", "-vvv","--verbose", help="Option used multiple times", action="count", default=0)
    parser.add_argument("-m", "--mode", type=int, choices=[0, 1, 2],
                    help="Select mode")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-y", "--yes", action="store_true", help="Exclusive with no")
    group.add_argument("-n", "--no", action="store_true", help="Exclusive with yes")

    #Add_argument
    #  (name or flags...)[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest]

    group.add_argument("--action1", "--action2",
        action="store",
        nargs=3,
        default="act1",
        type=str,
        choices=["act1", "act2", "act2"],
        required=False,
        help="The advanced option",
        metavar="PARAM",
        dest='other_var')

    args = parser.parse_args()
    main(args)

