input_file = '../any_text.txt'
output_file = '../names_from_file.txt'

myfile1 = open(input_file, mode='r', encoding='ascii')
myfile2 = open(output_file, mode='w', encoding='ascii')

# print(myfile.read())

name = 'Sasha'

for num, i in enumerate(myfile1):
	if name in i:
	    print(num, i.strip())
	    myfile2.write('From file: ' + str(num) + i)


mifile1.close()
mifile2.close()

