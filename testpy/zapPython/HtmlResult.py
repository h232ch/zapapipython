

import requests
 
headers = {
  'Accept': 'application/json',
  'X-ZAP-API-Key': 'dh24aid632odfbljoch8ng6dda'
}
r = requests.get('http://localhost:9000/OTHER/core/other/htmlreport/', params={
}, headers = headers)
 
 
# print (r.json())

# print(r.text)
 
f = open("./htmlparser/test.html", 'w')
data = r.text
f.write(data)
f.close
 
f = open("./htmlparser/test.html", 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()



# import requests
# headers = {
#   'Accept': 'application/json',
#   'X-ZAP-API-Key': 'dh24aid632odfbljoch8ng6dda'
# }
# 
# r = requests.get('http://localhost:9000/JSON/alert/view/alert/', params={
# 
# }, headers = headers)
# 
# print (r.text)
