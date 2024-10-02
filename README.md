# OM310-Domoticz-plugin
Domoticz plugin for OM-310 Power Limiter (Novatek-Elektro) over Modbus TCP

# Installation (openwrt)
opkg update

opkg install kmod-usb-serial-pl2303 mbusd domoticz python3 python3-pip nano

pip install pymodbus

ln -s /usr/lib/libpython3.11.so /usr/lib/libpython3.9.so

mkdir -p /opt/domoticz/plugins/OM310-Domoticz-plugin

wget -O /opt/domoticz/plugins/OM310-Domoticz-plugin/plugin.py https://raw.githubusercontent.com/tmrealive/OM310-Domoticz-plugin/refs/heads/main/plugin.py

chown -R domoticz:domoticz /opt/domoticz

nano /etc/config/domoticz
change option disabled to 0
change option userdata to /opt/domoticz

nano /etc/config/mbusd
change option enabled to 1

/etc/init.d/mbusd start
/etc/init.d/domoticz start

open domoticz site
add OM-310 device
