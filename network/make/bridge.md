# Bridge


## Command used

| Command | Description | Packet |
|- |- |
| ```brctl``` | Bridge control | bridge-utils |
| ```ip``` | Interface | iproute2 |
| ```nmctl``` | Network manager | ? |
| ```route``` | route table | ? |


nmcli conn add type bridge con-name br0 ifname br0

```bash
apt-get install bridge-utils

# Check actual interface using ip of iproute2
ip a
```

| Command | Description |
|- |- |
| ```brctl show``` | Dispaly bridge |
| ```brctl delbr br0``` | Delete bridge |
| ```nmcli conn show``` | Show all connetion |
| ```nmcli conn show --active``` | Show connetion active |


nmcli conn add type ethernet slave-type bridge con-name bridge-br0 





## Delete bridge

```ash
$ sudo ip link set enp1s0 up
$ sudo ip link set br0 down
$ sudo brctl delbr br0
```
