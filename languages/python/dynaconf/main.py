# coding: utf-8

from dynaconf import settings


def main():

    print(settings.SOME_VARIABLE)

    print(settings.get('SOME_VARIABLE'))


if __name__ == "__main__":
    main()