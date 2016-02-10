#!/usr/bin/env python
from PyOPC.OPCContainers import *
from PyOPC.XDAClient import XDAClient

def print_options((ilist,options)):
    print ilist; print options; print
    
address='http://192.168.5.2:8000/'

xda = XDAClient(OPCServerAddress=address,
                ReturnErrorText=True)

data = xda.Read([ItemContainer(ItemName='relay1_flow'),ItemContainer(ItemName='relay1_load'),ItemContainer(ItemName='relay1_breaker'),ItemContainer(ItemName='flag')])[0]
print data[0].Value
print data[1].Value
print data[2].Value
print data[3].Value

xda.Write([ItemContainer(ItemName='flag', Value='Captured i_virus')],LocaleID='en-us')

data = xda.Read([ItemContainer(ItemName='flag')])[0]
print data[0].Value


#print xda.Read([ItemContainer(ItemName='generation')])[0][0].Value
#print xda.Read([ItemContainer(ItemName='load')])[0][0].Value
#print xda.Read([ItemContainer(ItemName='breaker')])[0][0].Value
#print xda.Read([ItemContainer(ItemName='flow')])[0][0].Value
