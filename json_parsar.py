__author__ = 'venkat'

import json
import httplib2

global h

h = httplib2.Http(".cache")
h.add_credentials('admin', 'admin')

# Get the List of nodes available in the network
resp,content = h.request('http://localhost:8080/controller/nb/v2/hosttracker/default/hosts/active', 'GET')
nodes = json.loads(content.decode())
#print(json.dumps(nodes))
print(json.dumps(nodes, sort_keys=True, indent=2))


