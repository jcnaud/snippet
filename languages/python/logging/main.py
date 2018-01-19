#!/usr/bin/env python
# coding: utf-8

import logging
import logging.config
import os
import yaml

def setup_logging(
    default_path='logging.yaml',
    default_level=logging.INFO,
    env_key='LOG_CFG'
):
    """
    Setup logging configuration
    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


def main():
    setup_logging()

    # Here do some stuff ...
    logging.debug("Somme debug information")
    logging.info("Somme info information")
    logging.warning("Somme warning information")
    logging.error("Somme error information")

    try:
        1/0
    except Exception as e:
        logging.exception("Somme error + exception information : "+str(e))

    print(" === End of this programme ===")    


if __name__ == "__main__":
    main()


