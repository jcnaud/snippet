#!/usr/bin/env python
# coding: utf-8

import logging
import subprocess

def run_cmd(cmd):
    """
    Run a command
    if error, print and raise it
    params cmd : String command
    return out
    """
    logging.debug('Run command "'+cmd+'"')
    try:
        process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        process.check_returncode()
        
    except Exception as e:
        logging.exception(str(e) +"\nCMD_SHELL : "+cmd+"\nSTDOUT : "+process.stdout.decode()+"\nSTDERR : "+process.stderr.decode(), exc_info=True)
        #logging.critical("{CDM : "+cmd+", "} : "+cmd)
        #logging.critical("STDOUT : "+process.stdout.decode())
        #logging.critical("STDERR : "+process.stderr.decode())
        #raise e

    return process.stdout.decode()


def main():

    # Minimal logging configuration
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger(__name__).addHandler(logging.NullHandler())

     
    result = run_cmd("ls")
    print(result)

    result = run_cmd("ls un_fichier_qui_n_existe_pas")
    print(result)

    print(" === End of this programme ===")    

if __name__ == "__main__":
    main()
