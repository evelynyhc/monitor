import commands

def cpu():
	com='sar 3 3 | grep "Average"'
	number,state=commands.getstatusoutput(cmd=com)
	print(state)
	
	if number!=0:
		dict={'number':number}
	else:
		user=float(state.split()[2])
		nice=float(state.split()[3])
		system=float(state.split()[4])
		iowait=float(state.split()[5])
		steal=float(state.split()[6])
		idle=float(state.split()[7])
		dict={
			'number':number,
			'user':user,
			'nice':nice,
			'system':system,
			'iowait':iowait,
			'steal':steal,
			'idle':idle,
			}
	if user >= 50:
		print('yes')
	else:
		print('no')
	
	return dict
if __name__=='__main__':
	print(cpu())
