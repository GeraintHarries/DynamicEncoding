fileName = raw_input('Please enter the file you want to encode: ')

text = open(fileName, 'r').read()

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@$()_+-=.,<>/?;:\'"\\|]}[{`~ '

total = 0
acumulator = 0
dictionary = []
i = 0
tf = True
j = 0

for char in chars:
        count = text.count(char)
        if count >= 1:
                total += 1
                print char, count
                dictionary.insert(acumulator, char)
        acumulator += 1

while tf == True:
        if 2**j >= total:
                print "Encode with %i bits" % (j)
                tf = False
        j += 1

encodingDictionary = open('encodingDictionary.txt','w')

fullDictionary = {}

while i < len(dictionary):

	binary = bin(i).replace('0b', '')
	string = '{0:0>%s}' % (j-1)
	binaryFormat = string.format(binary)

	encodingDictionary.write("%s, %s; " % (binaryFormat, dictionary[i]))
	print "%s, \t %s" % (binaryFormat, dictionary[i])
	fullDictionary[dictionary[i]] = binaryFormat
	i += 1

print fullDictionary

decodedFile = open('decodedFile.txt', 'w')

with open('file.txt') as f:
  while True:
    c = f.read(1)
    if not c:
      print "End of file"
      break
    decodedFile.write(fullDictionary[c])











