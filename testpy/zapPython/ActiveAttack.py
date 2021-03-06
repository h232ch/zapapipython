'''
Created on 2020. 8. 23

@author: dnwn7
'''

#!/usr/bin/env python
import time
from pprint import pprint
from zapv2 import ZAPv2

apiKey = 'dh24aid632odfbljoch8ng6dda'
target = 'http://localhost:8000'
zap = ZAPv2(apikey=apiKey, proxies={'http': 'http://127.0.0.1:9000', 'https': 'http://127.0.0.1:9000'})

# TODO : explore the app (Spider, etc) before using the Active Scan API, Refer the explore section
print('Active Scanning target {}'.format(target))
scanID = zap.ascan.scan(target)
while int(zap.ascan.status(scanID)) < 100:
    # Loop until the scanner has finished
    print('Scan progress %: {}'.format(zap.ascan.status(scanID)))
    time.sleep(5)

print('Active Scan completed')
# Print vulnerabilities found by the scanning
print('Hosts: {}'.format(', '.join(zap.core.hosts)))
print('Alerts: ')
pprint(zap.core.alerts(baseurl=target))
