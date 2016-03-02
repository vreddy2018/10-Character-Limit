f = open('input.txt', 'r')
contents = f.readlines()
f.close()

f = open('output.txt', 'w')

for x in contents:

	x = x[0:10]

	print(x)
	
	f.write(x + '\n')

f.close()