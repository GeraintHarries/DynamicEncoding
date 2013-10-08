fileName = raw_input('Please enter the file you want to encode: ')

text = open(fileName, 'r').read()

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@$()_+-=.,<>/?;:\'"\\|]}[{`~ '

total = 0

for char in chars:
        count = text.count(char)
        if count >= 1:
                total += 1
                print char, count


print total

tf = True
i = 0

while tf == True:
        if 2**i >= total:
                print "Encode with %i bits" % (i)
                tf = False
        i += 1
