#!/usr/bin/env python
from PyOPC.OPCContainers import *
from PyOPC.XDAClient import XDAClient

def print_options((ilist,options)):
    print ilist; print options; print
    
address='http://192.168.1.200:8000/opc'

xda = XDAClient(OPCServerAddress=address,
                ReturnErrorText=True)

#print_options(xda.GetStatus())
#print_options(xda.Browse())
print_options(xda.Read([ItemContainer(ItemName='vat')]))
print_options(xda.Read([ItemContainer(ItemName='water_flow')]))
print_options(xda.Read([ItemContainer(ItemName='switch')]))
print_options(xda.Read([ItemContainer(ItemName='valve1')]))
