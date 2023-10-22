#!/usr/bin/env python
# coding: utf-8

import sys
import argparse
import textwrap
import logging
# Documentation https://docs.python.org/3/library/argparse.html

def parse_arguments(args):
    """
    Create parser and parse arguments
    If 'help' is selected, it print help and rise exit
    If condition is bad, it print a message problem and rise Exception.

    :return: Result of the parsing argument
    :rtype: argparse.Namespace
    """
    epilog = textwrap.dedent('''\
        Example of standard usage:
            Display help
                python ./cli.py --help
                python ./cli.py -h
            Example
              python ./cli.py -f config.yml -m 2 file_1 file_2 file_3
            
    ''')

    parser = argparse.ArgumentParser(
        prog='cli',
        description='Demo program of argparse',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=epilog)

    parser.add_argument(
        'files',
        help='List of files',
        metavar='FILES',
        type=str,
        nargs='+')  # Concatenate multiple arguments

    # Manage options
    parser.add_argument(
        '-f', '--input-file',
        help='input file',
        metavar='INPUT_FILE',
        default='settings.yml')  # No default mean this option is required

    parser.add_argument(
        '-m', '--mode',
        help="selected mode",
        metavar='MODE',
        type=int,
        choices=[0, 1, 2])

    group_vq = parser.add_mutually_exclusive_group()
    group_vq.add_argument(
        '-v', '--verbose',
        help='enable verbosity: -v = INFO, -vv = DEBUG',
        action='count',
        default=0)
    group_vq.add_argument(
        '-q', '--quiet',
        help="quiet mode",
        action="store_true")

    # Parse the arguments
    return parser.parse_args(args)


def main():
    # parse argument
    args = parse_arguments(sys.argv[1:])

    # Manage the logging verbosity
    if args.quiet:
        logging.basicConfig(level=logging.NOTSET)
    if args.verbose == 0:
        logging.basicConfig(level=logging.WARNING)
    if args.verbose == 1:
        logging.basicConfig(level=logging.INFO)
    elif args.verbose >= 2:
        logging.basicConfig(level=logging.DEBUG)

    # manage options
    if args.mode == 1:
        print('Mode is One')
    else:
        print('Mode is: {}'.format(args.mode))

    if args.files:
        print('files: {}'.format(args.files))
    else:
        print('No file passed')

    logging.warning('Some warning log')
    logging.info('Some info log')
    logging.debug('Some debug log')


def init():
    """Encapsulate if __name__ == '__main__' to make unit test more easily"""
    if __name__ == '__main__':
        sys.exit(main())


init()
