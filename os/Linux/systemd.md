# Systemd


## Links

Journalctl usefull: https://www.loggly.com/ultimate-guide/using-journalctl/

## Systemd 

Systemd manage service
systemctl is the command line interface of systemd
journald is the saervice managing lgo on all service
journalctl is the command line tool of journald


### Systemctl usage:

```bash
systemctl status
systemctl status sshd
# Display failed services
systemctl list-units --failed
systemctl list-units --state failed

# 
systemctl start sshd
systemctl stop sshd
systemctl restart sshd
systemctl status sshd
```

Default directory of systemd services: /lib/systemd/system

### Journalctl usage:

```bash

journalctl --since "1 hour ago"
journalctl -u nginx --since yesterday
journalctl -u nginx --until "2018-09-27 15:16:23"
journalctl -u nginx --since "2018-09-15" --until "2018-09-16"
journalctl -u nginx.service -u mysql.service
# Follow (tail -f like)
journalctl -f
# Since last boot
journalctl -b
# Since previous boot to last boot
journalctl -b -1
# List bost timestamp
journalctl --list-boots
```



