


USB issue:

If in first time the command ```hackrf_info``` give an error ```(-1000)``` but have no error in the next time you run this command.
That mean, the usb auto save power is activer for the hackrf and it is a problème.

Solution:

Link: https://github.com/mossmann/hackrf/wiki/FAQ#power-saving-and-usb-autosuspend


Add usbpid in blakc list to protect af usb power sage management


get pid hackrf ```lsusb```

Add in /etc/default/tlp :
```
USB_BLACKLIST="1111:2222"
```

Restart le service tlp : ``` sudo service tlp restart```