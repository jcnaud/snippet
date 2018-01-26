#!/bin/python
# coding: utf-8

import binascii
import struct
import re


def main():
    # In python, the <bytes> object represent binary data:
    # - "bytes" is a class/variable
    # - "bytes" have system représentation using symbology to be used in str (print, export, ...)


    # Exemple of symbology
    # - Hexa   : 'af92'
    # - Binary : '10010101101'
    # - ascii  : 'y\x00\x00|\xc6'

    # Two choices : 
    # - works always with 'str' with one symbology
    # - works always with 'bytes' with one system représentation (i.e. symbology)

    # Convertion :
    # - FROM 'str' + symbology A TO 'bytes' with symbology A   : theStr.encode()
    # - FROM 'bytes' with symbology 'A' TO 'str' + symbology A : theBytes.decode()
    



    # == Example with 'str' and with symbology 'hexa' 
    payload_hex = '2100000d757e034843457900007cc67a0000002a7b0000054b'

    # Slice this payloads by 5 bytes (10 hexa symbols)
    r = re.compile('([0-9abcdef]{10})')
    matchs = r.findall(payload_hex)

    for match in matchs:
        print(match)



    # == Example with 'bytes' and with symbology 'hexa'
    payload_bin = b'2100000d757e034843457900007cc67a0000002a7b0000054b'

    # Slice this payloads by 5 bytes (10 hexa symbols)
    r = re.compile(b'([0-9abcdef]{10})')
    matchs = r.findall(payload_bin)

    for match in matchs:
        print(match)        # Display : b'2100000d75'
        asc = binascii.unhexlify(match) # Change representation of bytes by ascii symbology (b'!\x00\x00\ru')
        print(type(asc))   # Always 'bytes'
        print(asc)

        # Structure: 
            # >  big-endian; (and forces concatenation and thus disable padding by bytes)
            # B  C:unsigned char, Python:integer 1 byte
            # L  C:unsigned long, Python:integer 4 bytes
        s = struct.Struct('>BL') 
        unpacked_data = s.unpack(asc)
        print(unpacked_data)


if __name__ == "__main__":
    main()
