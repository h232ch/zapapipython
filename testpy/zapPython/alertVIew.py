'''
Created on 2020. 8. 23

@author: dnwn7
'''

import requests
headers = {
  'Accept': 'application/json',
  'X-ZAP-API-Key': 'dh24aid632odfbljoch8ng6dda'
}

r = requests.get('http://localhost:9000/JSON/core/view/alertsSummary/', params={
}, headers = headers)
print (r.json())



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
