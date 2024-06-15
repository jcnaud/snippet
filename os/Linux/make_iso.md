# Make iso

- Use gparted to refromate the usb in fat32
- Download ISO
- Check the hash
- copy with ```dd if=theiso of=/dev/thepartition bs=1024k status=progress```
- Make sync ```sync```