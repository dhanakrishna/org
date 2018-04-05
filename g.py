values = [[3, 2222, 20, 122], [33, 6, 1, 2]]
 
v = values[0][0]
for row in range(0, len(values)):
#	print(row)
#	print(len(values[row]))
	for column in range(0, len(values[row])):
#		print(column)
		if v < values[row][column]:
			print(v)
			v = values[row][column]

print(v)			
