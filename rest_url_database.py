__author__ = 'venkat'

base_url = 'http://127.0.0.1:8080/'

'''
Specific URL's
'''
REST_URL_FOR_NODE = base_url + 'controller/nb/v2/switchmanager/default/nodes'
REST_URL_FOR_LINK = base_url + 'controller/nb/v2/switchmanager/default/node/OF/'
REST_URL_FOR_FLOW = base_url + 'controller/nb/v2/statistics/default/flow'
REST_URL_FOR_PORT = base_url + 'controller/nb/v2/statistics/default/port/node/OF/'
REST_URL_FOR_HOST = base_url + 'controller/nb/v2/hosttracker/default/hosts/active'

#REST_URL_FOR_PORT = base_url + 'controller/nb/v2/statistics/default/port'
