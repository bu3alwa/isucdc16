#Test Tags to see if this is actually working
#Syntax (name, failValue, cmp_op, [previous_nodes], [next_nodes], startValue)
tags = [('PS3_DEST_NET', '0', '==', None, ['PS5_PUMP_0', 'PS5_PUMP_1'], '1'),
		('PS5_PUMP_0', '0', '==', ['PS3_DEST_NET'], ['PS5_VALVE_0'], '1'),
		('PS5_PUMP_1', '0', '==', ['PS3_DEST_NET'], ['PS5_VALVE_1'], '1'),	
		('PS5_VALVE_0', '0', '==', ['PS5_PUMP_0'], ['PS5_DEST_NET'], '1'), 
		('PS5_VALVE_1', '0', '==', ['PS5_PUMP_1'], ['PS5_DEST_NET'], '1'),
		('PS5_DEST_NET', '0', '==', ['PS5_VALVE_1', 'PS5_VALVE_0'], None, '1')]
