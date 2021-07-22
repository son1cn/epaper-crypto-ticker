# epaper Crypto ticker

I had the idea to create a crypto ticker so I can monitor how the market is doing without needing my main computers to be on. To accomplish this, I bought an epaper display hat for a raspberry pi:

[PapiRus with 2.7in E-Ink Display](https://au.rs-online.com/web/p/raspberry-pi-screens/1218357/)

Start with a fresh [Raspbian Buster Lite image](https://downloads.raspberrypi.org/raspios_lite_armhf/images/raspios_lite_armhf-2021-05-28/2021-05-07-raspios-buster-armhf-lite.zip) (or whatever version is available now) with [SSH enabled](https://phoenixnap.com/kb/enable-ssh-raspberry-pi), set up a static IP (easiest from the DHCP server side) to make it easier to remote in later at a known address.

Using the install instructions linked on the store page [PapiRus on GitHub](https://github.com/PiSupply/PaPiRus) to install the drivers on the pi.
After following the automated install, **ensuring you select Python 2 and 3 when prompted**
>#### Auto Installation
>Just run the following script in a terminal window and PaPiRus will be automatically setup.
>```bash
># Run this line and PaPiRus will be setup and installed
>curl -sSL https://pisupp.ly/papiruscode | sudo bash
>```
#### Install python3 pip
```bash
sudo apt-get install python3-pip
```
#### Install [coingecko API](https://pypi.org/project/pycoingecko/)
```bash
pip3 install pycoingecko
```

I found another GitHub project [schech1/BTCDisplay](https://github.com/schech1/BTCDisplay) that is doing most of what I am after, so I started with their code.

