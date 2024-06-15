# Reset password


## Grub force access

- Reboot de serveur
- wait grub
- press 'e' to edit

add replace "ro quiet splash $vt_handoff"  to "rw init=/bin/bash" at the end of the line "start by "linux"


make change

reboot


## With live cd

```bash
mkdir /mnt/target
# Identify the disk
fdisk -l
# Mount it
mount /dev/sdb1 /mnt/target
# Chroot on it
chroot /mnt/target
password 

exit
# Safe umount
umount /dev/sdb1 /mnt/target
```
