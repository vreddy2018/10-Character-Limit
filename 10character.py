f = open('input.txt', 'r')
contents = f.readlines()
f.close()

f = open('output.txt', 'w')

count = 0
while count < len(contents):
	contents[count] = contents[count][:-1] 
	count += 1

for x in contents:

	x = x[0:10]

	print(x)

	f.write(x + '\n')

f.close()