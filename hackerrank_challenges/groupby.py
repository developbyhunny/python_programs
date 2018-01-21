from itertools import groupby
string =  input()

for char, times in groupby():
	print('('+char+', '+ str(times) +')')