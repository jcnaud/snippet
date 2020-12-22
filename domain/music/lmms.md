# LMMS

## Install

```bash
apt update
apt install lmms
```


## Addmidi keyboard

lsudb

Check linux module : ```lsmod```



amidi
aconnect 
aplaymidi


```
amidi -p hw:1,0,0 -S < `amidi -p hw:1,0,0 -d`
```

## Jack

http://linuxmao.org/Jack



### Qjackct

#### Install
```bash
apt install qjackcl
```
### Run
```bash
qjackctl
```

http://linuxmao.org/QJackCtl

Adavnaced tool : http://linuxmao.org/jack_tools

### Synth

Server : fluidsynth
GUI : qsynth
Midi sound font :  fluid-soundfont-gm

Install
```
apt install fluid-soundfont-gm fluidsynth qsynth
```
## 
Run it : ```qsynth```
Configure:
- (button) Configuration
  - (tab) MIDI -> Change driver midi to alsa_seq
  - (tab) audi -> Change audio driver to alsa
  - (tab) Sound font -> Load font : /usr/share/sounds/sf2/FluidR3_GM.sf2
- Restart qsynth to be sure configuration is apply
- Now you can connect your midi keyboard to qsynth with qjack



