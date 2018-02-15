
#!/usr/bin/env python
# coding: utf-8

import logging
import os
import subprocess

def real_time_cmd(cmd, cwd="."):
    """
    Run real time command, NOT WORKING WITH Pyton2 !!
    params cmd : String command
    params cwd : Path command
    yield: line by line stdout and stderr
    """

    process = subprocess.Popen(
                cmd,
                bufsize=1,
                shell=True,
                stdout=subprocess.PIPE,    # PIPE the output
                stdin=open(os.devnull),    # Disable input
                stderr=subprocess.STDOUT,  # PIPE the stderr to the stdout
                universal_newlines=True,
                cwd=cwd
            )
    stdout = process.stdout # Get the PIPE (yield line)

    for line in stdout:
        yield line # Retourn line by line

def main():
    # Minimal logging configuration
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger(__name__).addHandler(logging.NullHandler())

    for line in real_time_cmd("echo 'hahaha' && sleep 1 && echo 'hohoho' && sleep 1"):
        print(line) 

    for line in real_time_cmd("ls un_fichier_qui_n_existe_pas"):
        print(line) 

    print(" === End of this programme ===")    

if __name__ == "__main__":
    main()
