#!/usr/bin/env python
"""
OM-310 Power Limiter
Original author: tmr
Requirements: pymodbus
"""
"""
<plugin key="OM310" name="OM-310 Novatek-Elektro Power Limiter" version="0.0.1" author="tmr">
    <params>
        <param field="Address" label="IP Address" width="160px" required="true" default="127.0.0.1" />
        <param field="Port" label="Port" width="40px" required="true" default="502" />
        <param field="Mode1" label="Device Address" width="40px" required="true" default="1" />
        <param field="Mode2" label="Heartbeat" width="40px" required="true" default="10" />
        <param field="Mode3" label="Base Energy" width="80px" required="true" default="0" />
    </params>
</plugin>
"""

import Domoticz
from pymodbus.client import ModbusTcpClient

class BasePlugin:
    def __init__(self):
        self.runInterval = 1
        self.om310 = None
        return

    def onStart(self):
        Domoticz.Log("OM310 plugin start")
 
        if 1 not in Devices: Domoticz.Device(Name="Current L1 (IF1)",Unit=1,TypeName="Custom",Used=1,Options={"Custom":"1;A"}).Create()
        if 2 not in Devices: Domoticz.Device(Name="Current L2 (IF2)",Unit=2,TypeName="Custom",Used=1,Options={"Custom":"1;A"}).Create()
        if 3 not in Devices: Domoticz.Device(Name="Current L3 (IF2)",Unit=3,TypeName="Custom",Used=1,Options={"Custom":"1;A"}).Create()
        if 4 not in Devices: Domoticz.Device(Name="Zero Sequence Current (IF0)",Unit=4,TypeName="Custom",Used=0,Options={"Custom":"1;A"}).Create()
        if 5 not in Devices: Domoticz.Device(Name="Average Current L1 (IS1)",Unit=5,TypeName="Custom",Used=0,Options={"Custom":"1;A"}).Create()
        if 6 not in Devices: Domoticz.Device(Name="Average Current L2 (IS2)",Unit=6,TypeName="Custom",Used=0,Options={"Custom":"1;A"}).Create()
        if 7 not in Devices: Domoticz.Device(Name="Average Current L3 (IS3)",Unit=7,TypeName="Custom",Used=0,Options={"Custom":"1;A"}).Create()
        if 8 not in Devices: Domoticz.Device(Name="Maximum Current L1 (IN1)",Unit=8,TypeName="Custom",Used=0,Options={"Custom":"1;A"}).Create()
        if 9 not in Devices: Domoticz.Device(Name="Maximum Current L2 (IN2)",Unit=9,TypeName="Custom",Used=0,Options={"Custom":"1;A"}).Create()
        if 10 not in Devices: Domoticz.Device(Name="Maximum Current L3 (IN3)",Unit=10,TypeName="Custom",Used=0,Options={"Custom":"1;A"}).Create()
        if 11 not in Devices: Domoticz.Device(Name="Negative Sequence Current (IOP)",Unit=11,TypeName="Custom",Used=0,Options={"Custom":"1;A"}).Create()

        if 12 not in Devices: Domoticz.Device(Name="Voltage L1 (UF1)",Unit=12,TypeName="Custom",Used=1,Options={"Custom":"1;V"}).Create()
        if 13 not in Devices: Domoticz.Device(Name="Voltage L2 (UF2)",Unit=13,TypeName="Custom",Used=1,Options={"Custom":"1;V"}).Create()
        if 14 not in Devices: Domoticz.Device(Name="Voltage L3 (UF3)",Unit=14,TypeName="Custom",Used=1,Options={"Custom":"1;V"}).Create()
        if 15 not in Devices: Domoticz.Device(Name="Line Voltage L12 (UL1)",Unit=15,TypeName="Custom",Used=0,Options={"Custom":"1;V"}).Create()
        if 16 not in Devices: Domoticz.Device(Name="Line Voltage L23 (UL2)",Unit=16,TypeName="Custom",Used=0,Options={"Custom":"1;V"}).Create()
        if 17 not in Devices: Domoticz.Device(Name="Line Voltage L31 (UL3)",Unit=17,TypeName="Custom",Used=0,Options={"Custom":"1;V"}).Create()
        if 18 not in Devices: Domoticz.Device(Name="Positive Sequence Voltage (UPP)",Unit=18,TypeName="Custom",Used=0,Options={"Custom":"1;V"}).Create()
        if 19 not in Devices: Domoticz.Device(Name="Negative Sequence Voltage (UOP)",Unit=19,TypeName="Custom",Used=0,Options={"Custom":"1;V"}).Create()
        if 20 not in Devices: Domoticz.Device(Name="Zero Sequence Voltage (UNP)",Unit=20,TypeName="Custom",Used=0,Options={"Custom":"1;V"}).Create()

        if 21 not in Devices: Domoticz.Device(Name="Apparent Power (POT)",Unit=21,TypeName="Custom",Used=0,Options={"Custom":"1;kVA"}).Create()
        if 22 not in Devices: Domoticz.Device(Name="Active Power (POA)",Unit=22,TypeName="Custom",Used=1,Options={"Custom":"1;kW"}).Create()
        if 23 not in Devices: Domoticz.Device(Name="Reactive Power (POJ)",Unit=23,TypeName="Custom",Used=0,Options={"Custom":"1;kVAR"}).Create()
        if 24 not in Devices: Domoticz.Device(Name="Active Power L1 (PAA)",Unit=24,TypeName="Custom",Used=1,Options = {"Custom":"1;kW"}).Create()
        if 25 not in Devices: Domoticz.Device(Name="Active Power L2 (PAB)",Unit=25,TypeName="Custom",Used=1,Options = {"Custom":"1;kW"}).Create()
        if 26 not in Devices: Domoticz.Device(Name="Active Power L3 (PAC)",Unit=26,TypeName="Custom",Used=1,Options = {"Custom":"1;kW"}).Create()

        if 27 not in Devices: Domoticz.Device(Name="Cosine L1 (PCA)",Unit=27,TypeName="Custom",Used=0,Options={"Custom":"1;°"}).Create()
        if 28 not in Devices: Domoticz.Device(Name="Cosine L2 (PCB)",Unit=28,TypeName="Custom",Used=0,Options={"Custom":"1;°"}).Create()
        if 29 not in Devices: Domoticz.Device(Name="Cosine L3 (PCC)",Unit=29,TypeName="Custom",Used=0,Options={"Custom":"1;°"}).Create()

        if 30 not in Devices: Domoticz.Device(Name="Overload Timer Off (T0P)",Unit=30,TypeName="Custom",Used=0,Options={"Custom":"1;s"}).Create()
        if 31 not in Devices: Domoticz.Device(Name="Automatic Timer On (TAP)",Unit=31,TypeName="Custom",Used=0,Options={"Custom":"1;s"}).Create()
        if 32 not in Devices: Domoticz.Device(Name="Overload Timer On (TTP)",Unit=32,TypeName="Custom",Used=0,Options={"Custom":"1;s"}).Create()

        if 33 not in Devices: Domoticz.Device(Name="Frequency (FFF)",Unit=33,TypeName="Custom",Used=0,Options={"Custom":"1;Hz"}).Create()

        if 34 not in Devices: Domoticz.Device(Name="Energy L1",Unit=34,TypeName="Custom",Used=0,Options={"Custom":"1;kVA/h"}).Create()
        if 35 not in Devices: Domoticz.Device(Name="Energy L2",Unit=35,TypeName="Custom",Used=0,Options={"Custom":"1;kVA/h"}).Create()
        if 36 not in Devices: Domoticz.Device(Name="Energy L3",Unit=36,TypeName="Custom",Used=0,Options={"Custom":"1;kVA/h"}).Create()
        if 37 not in Devices: Domoticz.Device(Name="Energy",Unit=37,TypeName="Custom",Used=0,Options={"Custom":"1;kVA/h"}).Create()

        self.om310 = ModbusTcpClient(Parameters["Address"], port=Parameters["Port"], timeout=1)
 
        Domoticz.Heartbeat(int(Parameters["Mode2"]))

    def onStop(self):
        if self.om310.is_socket_open(): self.om310.close()

        Domoticz.Log("OM310 plugin stop")

    def onHeartbeat(self):
        if not self.om310.is_socket_open(): self.om310.connect()

        dataCurrent = self.om310.read_holding_registers(100,11,int(Parameters["Mode1"]))
        itemIF1 = dataCurrent.registers[0] / 10
        itemIF2 = dataCurrent.registers[1] / 10
        itemIF3 = dataCurrent.registers[2] / 10
        itemIF0 = dataCurrent.registers[3] / 10
        itemIS1 = dataCurrent.registers[4] / 10
        itemIS2 = dataCurrent.registers[5] / 10
        itemIS3 = dataCurrent.registers[6] / 10
        itemIN1 = dataCurrent.registers[7] / 10
        itemIN2 = dataCurrent.registers[8] / 10
        itemIN3 = dataCurrent.registers[9] / 10
        itemIOP = dataCurrent.registers[10] / 10
        
        dataVoltage = self.om310.read_holding_registers(111,9,int(Parameters["Mode1"]))
        itemUF1 = dataVoltage.registers[0]
        itemUF2 = dataVoltage.registers[1]
        itemUF3 = dataVoltage.registers[2]
        itemUL1 = dataVoltage.registers[3]
        itemUL2 = dataVoltage.registers[4]
        itemUL3 = dataVoltage.registers[5]
        itemUPP = dataVoltage.registers[6]
        itemUOP = dataVoltage.registers[7]
        itemUNP = dataVoltage.registers[8]

        dataPower = self.om310.read_holding_registers(120,12,int(Parameters["Mode1"]))
        itemPOT = (dataPower.registers[0] + dataPower.registers[1]) / 100
        itemPOA = (dataPower.registers[2] + dataPower.registers[3]) / 100
        itemPAA = (dataPower.registers[4] + dataPower.registers[5]) / 100
        itemPAJ = (dataPower.registers[6] + dataPower.registers[7]) / 100
        itemPAA = (dataPower.registers[8] + dataPower.registers[9]) / 100
        itemPAC = (dataPower.registers[10] + dataPower.registers[11]) / 100
        
        dataCosine = self.om310.read_holding_registers(132,3,int(Parameters["Mode1"]))
        itemPCA = dataCosine.registers[0] / 1000
        itemPCB = dataCosine.registers[1] / 1000
        itemPCC = dataCosine.registers[2] / 1000
        
        dataTimer = self.om310.read_holding_registers(135,4,int(Parameters["Mode1"]))
        itemT0P = dataTimer.registers[0]
        itemTAP = dataTimer.registers[1]
        itemTTP = dataTimer.registers[2]
        itemFFF = dataTimer.registers[3] / 10

        dataEnergy = self.om310.read_holding_registers(90,6,int(Parameters["Mode1"]))
        itemEL1 = (dataEnergy.registers[0] + dataEnergy.registers[1]) / 10
        itemEL2 = (dataEnergy.registers[2] + dataEnergy.registers[3]) / 10
        itemEL3 = (dataEnergy.registers[4] + dataEnergy.registers[5]) / 10
        itemEL0 = itemEL1 + itemEL2 + itemEL3 + float(Parameters["Mode3"])
        
        Devices[1].Update(0,str(itemIF1))
        Devices[2].Update(0,str(itemIF2))
        Devices[3].Update(0,str(itemIF3))
        Devices[4].Update(0,str(itemIF0))
        Devices[5].Update(0,str(itemIS1))
        Devices[6].Update(0,str(itemIS2))
        Devices[7].Update(0,str(itemIS3))
        Devices[8].Update(0,str(itemIN1))
        Devices[9].Update(0,str(itemIN2))
        Devices[10].Update(0,str(itemIN3))
        Devices[11].Update(0,str(itemIOP))

        Devices[12].Update(0,str(itemUF1))
        Devices[13].Update(0,str(itemUF2))
        Devices[14].Update(0,str(itemUF3))
        Devices[15].Update(0,str(itemUL1))
        Devices[16].Update(0,str(itemUL2))
        Devices[17].Update(0,str(itemUL3))
        Devices[18].Update(0,str(itemUPP))
        Devices[19].Update(0,str(itemUOP))
        Devices[20].Update(0,str(itemUNP))

        Devices[21].Update(0,str(itemPOT))
        Devices[22].Update(0,str(itemPOA))
        Devices[23].Update(0,str(itemPAA))
        Devices[24].Update(0,str(itemPAJ))
        Devices[25].Update(0,str(itemPAA))
        Devices[26].Update(0,str(itemPAC))
        Devices[27].Update(0,str(itemPCA))
        Devices[28].Update(0,str(itemPCB))
        Devices[29].Update(0,str(itemPCC))

        Devices[30].Update(0,str(itemT0P))
        Devices[31].Update(0,str(itemTAP))
        Devices[32].Update(0,str(itemTTP))
        Devices[33].Update(0,str(itemFFF))

        Devices[34].Update(0,str(itemEL1))
        Devices[35].Update(0,str(itemEL2))
        Devices[36].Update(0,str(itemEL3))
        Devices[37].Update(0,str(itemEL0))

global _plugin
_plugin = BasePlugin()

def onStart():
    global _plugin
    _plugin.onStart()

def onStop():
    global _plugin
    _plugin.onStop()

def onHeartbeat():
    global _plugin
    _plugin.onHeartbeat()
