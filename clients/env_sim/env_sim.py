#!/usr/bin/env python
from PyOPC.OPCContainers import *
from PyOPC.XDAClient import XDAClient
import random, time
import math

address='http://192.168.1.200:8000/opc'

xda = XDAClient(OPCServerAddress=address,
               ReturnErrorText=True)

def initial_fill():
	for i in range(0,4):
		xda.Write([ItemContainer(ItemName='vat',Value=i*10)])
		time.sleep(2);

def make_write(name, value):
	xda.Write([ItemContainer(ItemName=name,Value=value)])

def update_sim():
	(ilist0,options0) = xda.Read([ItemContainer(ItemName='vat')]);
	(ilist1,options1) = xda.Read([ ItemContainer(ItemName='water_flow')]); 
	(ilist2,options2) = xda.Read([ItemContainer(ItemName='switch')]);
	print ilist1[0].Value
	if(int(ilist2[0].Value) == 1 and int(ilist0[0].Value) > 90):
		make_write('vat', .1)
	else:
		change = random.randrange(1,4)%2;		
		entropy = random.randrange(0,4);
		if(change == 1):
			newvalue = int(ilist0[0].Value) + (math.floor(int(ilist1[0].Value)/100)*entropy)+1;
			print 'newvalue=' + str(newvalue);
			if(newvalue > 100 and int(ilist2[0].Value) == 1):
				make_write('vat', 0.1);
			else:
				make_write('vat', newvalue);
		else:
			newvalue = int(ilist0[0].Value) - math.floor(int(ilist1[0].Value)/100)-1;
			print 'newvalue=' + str(newvalue);
			if(newvalue < 0):
				make_write('vat', 0.1);
			else:
				make_write('vat', newvalue);

initial_fill();
while(1):
	time.sleep(5);
	print("Changing value\n");
	update_sim();
