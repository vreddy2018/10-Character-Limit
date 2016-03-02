f = open('input.txt', 'r')
contents = f.readlines()
for x in contents:
	if len(x) > 10:
		x = x[0:10]
		print(x)
