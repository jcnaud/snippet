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



import subprocess

with subprocess.Popen(
    "java",
    shell=True,
    stdout=subprocess.PIPE,
    stdin=subprocess.DEVNULL,
    stderr=subprocess.STDOUT,
    #encoding="utf-8",
    #universal_newlines=True
) as proc:
    for raw in proc.stdout:
        line = raw.decode('cp1256')
        print(raw)
        print(line)
        #print('{} {}'.format(type(line), line))



import subprocess

with subprocess.Popen(
    "java",
    shell=True,
    stdout=subprocess.PIPE,
    stdin=subprocess.DEVNULL,
    stderr=subprocess.STDOUT,
    encoding="utf-8",
    universal_newlines=True
) as proc:
    for raw in proc.stdout.read_line():
        line = raw
        print(line)
        #print('{} {}'.format(type(line), line))




import subprocess

with subprocess.Popen(
    "javatt",
    shell=True,
    stdout=subprocess.PIPE,
    stdin=subprocess.DEVNULL,
    stderr=subprocess.STDOUT,
    universal_newlines=True

    encoding="utf-8",
) as proc:
    for raw in proc.stdout:
        line = raw
        #print('{}'.format(type(line)))
        print('{}'.format(line))






import subprocess

endocing_list = ["cp850", "cp1252", "utf-8"]
with subprocess.Popen(
    "javatt",
    shell=True,
    stdout=subprocess.PIPE,
    stdin=subprocess.DEVNULL,
    stderr=subprocess.STDOUT
    #encoding='cp1256'
) as proc:
    for raw in proc.stdout:
        for endoding in endocing_list:
            line = None
            print(endoding)
            try:
                line = raw.decode(endoding)
                break
            except:
                pass
        if line:
            #print('{}'.format(type(line)))
            print('{}'.format(line))



    for encoding in endocing_list:
        print(encoding)
        try:
            return_string = output.decode(encoding).strip()
            print(return_string)
        except:
            print("exception happened")
            return_string = ""


"C:\Program Files (x86)\Common Files\Oracle\Java\javapath\java.exe" -jar bin\chloe-4.0.jar "C:/Users/jnaud/Documents/temp/37_INRA/chloe/output_from_csv/v4.properties"
