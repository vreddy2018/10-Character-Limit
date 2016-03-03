f = open('input.txt', 'r')
contents = f.readlines()
f.close()

f = open('output.txt', 'w')


for x in contents:

	x = x[0:10] #only keeps characters between 0 and 10
	x = x.strip('\n') #gets rid of \n so that empty lines wont be printed
	
	print(x)

	f.write(x + '\n')

f.close()