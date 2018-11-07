# coding: utf-8


from scapy.all import *


def main():
    """sniff function"""
    sniff(iface='eth0', prn=http_header, filter="tcp port 80")
    p = IP(dst="github.com")/TCP()
    r = sr1(p)
    print(r.summary())

if __name__ == '__main__':
    main()

a=sniff(filter="tcp and ( port 25 or port 443 )",
  prn=lambda x: x.sprintf("%IP.src%:%TCP.sport% -> %IP.dst%:%TCP.dport%  %2s,TCP.flags% : %TCP.payload%"))

# get iface name with the command ifaces
sniff(iface=16, prn=lambda x: x.show(), filter="tcp")

ip.addr == 193.158.231.216
