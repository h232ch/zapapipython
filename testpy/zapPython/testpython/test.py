'''
Created on 2020. 8. 23

@author: dnwn7
'''

f = open("../htmlparser/test.html", 'w')
data = "test"
f.write(data)
f.close

f = open("../htmlparser/test.html", 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()