fileName = raw_input('Please enter the file you want to encode: ')

text = open(fileName, 'r').read()

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@$()_+-=.,<>/?;:\'"\\|]}[{`~ '

total = 0
acumulator = 0


dictionary = []

for char in chars:
        count = text.count(char)
        if count >= 1:
                total += 1
                print char, count
                dictionary.insert(acumulator, char)
        acumulator += 1

i = 0

tf = True
j = 0

while tf == True:
        if 2**j >= total:
                print "Encode with %i bits" % (j)
                tf = False
        j += 1

encodingDictionary = open('encodingDictionary.txt','w')

while i < len(dictionary):
	binary = bin(i).replace('0b', '')
	binaryFormat = "{0:0>4}".format(binary)

	encodingDictionary.write("%s, %s; " % (binaryFormat, dictionary[i]))
	print "%s, \t %s" % (binaryFormat, dictionary[i])
	i += 1





