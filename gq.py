def ma(lst):
	v = lst[0]
	for e in lst:
		if v < e: 
			v = e
	return v

e=[[3,4,5,1],[33,6,1,2]]
for row in e:
	#print(row)
	print(ma(row))


