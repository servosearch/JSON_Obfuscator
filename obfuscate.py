# JSON obfuscator 

import re
import json

def unicode_8bit(ch): #Changing decimal Unicode code point to 8-bit.
    return '\\u{:04x}'.format(ord(ch)) 

fileName = input('Please enter the name of input file below (w/o extension): \n')
# fileName='input'
with open('%s.json' % fileName, 'r') as j:
    rawData = json.dumps((json.load(j)), sort_keys=False,indent=4) #Json conversion to string

#Lets try regex
result = re.findall("\"([^\"]*)\"", rawData) #List of strigs

bitwords = [] #List of changed 8bit values
for a in result:
    bitword =""
    for i in a:
        value = unicode_8bit(i)
        bitword += str(value)
    bitwords.append(bitword)


output1 = open('replacement mapping file.txt', 'w+')
for i in range(len(result)):
    output1.write(result[i]+" ---> "+bitwords[i]+"\n")
output1.close


output2= open('obfuscated.json', 'w+')
for i in range(len(result)):
    rawData=re.sub(result[i], repr(bitwords[i]), rawData)
    print(result[i]+" "+bitwords[i])  
rawData=re.sub("'","", rawData) # repr adds unnecessary '', regex used to revert , this line should be optimized in the future.
output2.write(rawData)
output2.close

input("Process is over. Press any key. Please check obfuscated.json and replacement mapping file.txt for tranlation.")
# output2= open('obfuscated.json', 'w+')
# for i in rawData:                     #Iteration method, int and Booleans are included
#     if i.isalnum() == False:
#         output2.write(i)
#     elif isinstance(i,(bool,int)):
#         output2.write(i)
#     else:                  
#         value = unicode_8bit(i)
#         output2.write(value)
# output2.close