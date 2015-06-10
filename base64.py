import base64

word = raw_input("please input string : ")

word = base64.encode(word)

print "Encoded = " + word
