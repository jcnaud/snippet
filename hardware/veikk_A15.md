# Veikk A15 tablette driver install on linux

<!-- TOC -->

- [Veikk A15 tablette driver install on linux](#veikk-a15-tablette-driver-install-on-linux)
  - [Fix the tablette area to one screen](#fix-the-tablette-area-to-one-screen)
  - [Intall driver on linux](#intall-driver-on-linux)
    - [Check file installed](#check-file-installed)
    - [See log Veikk by chek bus event](#see-log-veikk-by-chek-bus-event)
    - [Bug hid-generic stole the usb device](#bug-hid-generic-stole-the-usb-device)

<!-- /TOC -->


## Fix the tablette area to one screen

List usb input on linux and get the **id**. Ex: **19**
```bash
xinput
```
Result
```
⎡ Virtual core pointer                    	id=2	[master pointer  (3)]
⎜   ↳ VEIKK.INC A15                           	id=19	[slave  pointer  (2)]
```

Display monitors and get the **name**. Ex: **eDP-1-1**
```bash
xrandr
#or 
xrandr --listmonitors
```

Result
```
Monitors: 2
 0: +*eDP-1-1 1920/344x1080/193+1920+0  eDP-1-1
 1: +DP-1-1 1920/531x1080/299+0+0  DP-1-1
```

Fix graphical tablette to the choosed screen
```bash
xinput map-to-output 19 eDP-1-1
```

or

xinput map-to-output $(xinput list --id-only "VEIKK A15 Pen Pen (0)") DP-1-1


## Intall driver on linux

Unofficial source : https://github.com/jlam55555/veikk-linux-driver


```bash
git clone https://github.com/jlam55555/veikk-linux-driver.git
cd veikk-linux-driver
sudo apt update
sudo apt-get install linux-generic linux-headers-`uname -r` build-essential libelf-dev
```
You have these file
- README.md
- Makefile
- veikk_drv.c
- veikk.h
- veikk_modparms.c
- veikk_vdev.c


```bash
make all
sudo make install
make clean
```
This error is normal because the module is not certified
```
- SSL error:02001002:system library:fopen:No such file or directory: ../crypto/bio/bss_file.c:72
- SSL error:2006D080:BIO routines:BIO_new_file:no such file: ../crypto/bio/bss_file.c:79
sign-file: certs/signing_key.pem: No such file or directory
  DEPMOD  4.15.0-112-generic
```

### Check file installed
Check module exist
```bash
sudo ls -al /etc/modules-load.d/veikk.conf
```

Check module loaded
```bash
egrep -i veikk /proc/modules
```


Check bus driver exist
```bash
ls /sys/bus/hid/drivers/veikk/
```

You can see other common driver (not veikk) by this command
```bash
ls /sys/bus/hid/drivers/
ls /sys/bus/hid/drivers/hid-generic/
```


### See log Veikk by chek bus event

evtest alow to see log driver event activity
```bash
apt install evtest
sudo evtest
```

Select one of these input
```
/dev/input/event20:     VEIKK A15 Pen
/dev/input/event21:     VEIKK A15 Pen
/dev/input/event22:     VEIKK A15 Pen
```

For le 20, i see when pen touch with ABS_PRESSURE
```
Event: time 1602159703.484700, -------------- SYN_REPORT ------------
Event: time 1602159703.488698, type 3 (EV_ABS), code 24 (ABS_PRESSURE), value 5899
```


### Bug hid-generic stole the usb device

Link: https://github.com/jlam55555/veikk-linux-driver/issues/2

List device veikk driver loaded in xxxx:2FEB:xxxx.xxxx with :
```
ls /sys/bus/hid/drivers/veikk | egrep 2FEB
````
Result:
```
0003:2FEB:0004.0007
0003:2FEB:0004.0008
0003:2FEB:0004.0009
```

If this is not the case, black list VEIKK A15 to hid-generic
```
echo -n "xxxx:2FEB:000x.xxxx" > /sys/bus/hid/drivers/hid-generic/unload



## GUI mot tested

```bash
sudo apt install qt5-qmake
git clone https://github.com/jlam55555/veikk-linux-driver-gui
cd veikk-linux-driver-gui
sudo apt update && apt install qt5-defaukt qt5-qmake
```

qmake && make all clean
sudo ./veikk-linux-driver-gui

