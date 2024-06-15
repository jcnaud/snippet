# dd

DD is a tools to copy partition


## Link:
Create bootable USB: https://www.cyberciti.biz/faq/creating-a-bootable-ubuntu-usb-stick-on-a-debian-linux/
## Usage

Connect your usb key

```bash
# Identify partitions
cat /proc/partitions
ls -1 /dev/sd*
lsblk

sudo dmesg
```



As root
```bash
# Copy iso to partition sdb. WARNING, THIS COMMAND ERASE SDB
# (if) is input
# (of) is output. WILL BE ERASED
# Copy by block of 8M (bs=) and show progress (status=)
# Add sync to valdiate peripherique sync
dd if=your.iso of=/dev/sdb bs=8M status=progress && sync

# It take 1 or 2 minutes
```


### Format usb disk
```bash
# Display
lsblk
# umount
umount /dev/sdb5
```

As user
```bash
# Run gparted
gparted
# - Crete new partition table
# - Create partion with fat32 format
# - Apply
```


### Check result
As user
```bash
lsblk


```
