# Wake-on-lan

Wake-On-Lan (WOL) allow to start physical computer using ethernet.
Work with ethernet.


## Link

Usefull site: https://www.cyberciti.biz/tips/linux-send-wake-on-lan-wol-magic-packets.html

## Activacte on BIOS


## Install [Debian like]

As root:
```bash
# Install client
apt install wakeonlan
```

## Install [RH like]
As root:
```bash
# Install client
apt install etherwake
```

## Usage

```bash
# Send message 
etherwake MAC-Address-Here
# Get Max address with ip
ping -c 4 192.168.0.253 && arp -n

```

Save mac adress somewhere
