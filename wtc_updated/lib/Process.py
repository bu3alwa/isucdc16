#!/usr/bin/env python

import ast, copy
from PyOPC.OPCContainers import *

'''def create_state_compare(logic, failValue):
	def CheckFailed(cur):
		source = str(failValue) + logic + str(cur)
		node = ast.parse(source, mode='eval')
		return eval(compile(node, '<string>', mode='eval'))
	return CheckFailed'''
    
def checkFailed(failValue, cur):
    return failValue == cur

class ProcessObject:
	def __init__(self, name, failValue, depends, next_list, cur=0, state=True):
		self.name = name
		self.dep_list = depends
		self.next_list = next_list
		self.nnodes = []
		self.depends = []
		self.failValue = failValue
		self.state = state
		#self.checkFailed = create_state_compare(cmp_op, self.failValue)
		self.cur = cur
		self.dirty = False

	def UpdateState(self, cur):
		self.cur = cur
		if not self.checkFailed(self.failValue, cur):
			self.state = True
		else:
			self.state = False

	def Online(self):
		return self.state





