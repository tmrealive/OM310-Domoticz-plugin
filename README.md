# OM310-Domoticz-plugin
Domoticz plugin for OM-310 Power Limiter (Novatek-Elektro) over Modbus TCP

![OM310-Domoticz-plugin](https://raw.githubusercontent.com/tmrealive/OM310-Domoticz-plugin/refs/heads/main/plugin.png)

# Installation (openwrt, pl2303 usb modbus adapter)
1. Install dependencies
```
opkg update
opkg install kmod-usb-serial-pl2303 mbusd domoticz python3 python3-pip nano
pip install pymodbus
```
2. Fix broken
```
ln -s /usr/lib/libpython3.11.so /usr/lib/libpython3.9.so
```
3. Download plugin
```
mkdir -p /opt/domoticz/plugins/OM310-Domoticz-plugin
wget -O /opt/domoticz/plugins/OM310-Domoticz-plugin/plugin.py https://raw.githubusercontent.com/tmrealive/OM310-Domoticz-plugin/refs/heads/main/plugin.py
chown -R domoticz:domoticz /opt/domoticz
```
4. Edit configs
- /etc/config/domoticz
  - change option disabled to 0
  - change option userdata to /opt/domoticz

- /etc/config/mbusd
  - change option enabled to 1

5. Start services
```
/etc/init.d/mbusd start
/etc/init.d/domoticz start
```

# Configuration
Open domoticz site and add OM-310 device

![OM310-Domoticz-plugin setup](https://raw.githubusercontent.com/tmrealive/OM310-Domoticz-plugin/refs/heads/main/setup.png)

# Documentation
[Power limiter OM-310 Users manual](OM-310_EN.pdf)
