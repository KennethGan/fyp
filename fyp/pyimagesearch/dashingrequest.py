#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests  # pip install requests
import simplejson as json  # pip install simplejson
from urllib import request, parse

url = 'http://localhost:3030'
headers = {'Content-type': 'application/json'}


class dashingrequest:

    def updatecarstats(self, cartotalplus, cartotalminus):

        widget = 'totalcarcount'
        data = {'auth_token': 'YOUR_AUTH_TOKEN',
                'text': str(cartotalplus + cartotalminus)}

        fullUrl = '%s/widgets/%s' % (url, widget)

        requests.post(fullUrl, data=json.dumps(data), headers=headers)

    def updatestatusstats(self, status):

        widget = 'trafficstatus'
        data = {'auth_token': 'YOUR_AUTH_TOKEN', 'text': status}

        fullUrl = '%s/widgets/%s' % (url, widget)

        requests.post(fullUrl, data=json.dumps(data), headers=headers)

    def updatebikestats(self, biketotalplus, biketotalminus):

        widget = 'totalbikecount'
        data = {'auth_token': 'YOUR_AUTH_TOKEN',
                'text': str(biketotalplus + biketotalminus)}

        fullUrl = '%s/widgets/%s' % (url, widget)

        requests.post(fullUrl, data=json.dumps(data), headers=headers)

    def updatetotalcount(self, totalcount):

        widget = 'totalcount'
        data = {'auth_token': 'YOUR_AUTH_TOKEN',
                'text': str(totalcount)}

        fullUrl = '%s/widgets/%s' % (url, widget)

        requests.post(fullUrl, data=json.dumps(data), headers=headers)

    def updatetrafficstatus(self, trafficstatus):

        widget = 'trafficstatus'
        data = {'auth_token': 'YOUR_AUTH_TOKEN', 'text': trafficstatus}

        fullUrl = '%s/widgets/%s' % (url, widget)

        requests.post(fullUrl, data=json.dumps(data), headers=headers)


    def updatetrafficvolume(self, detections):

        widget = 'trafficvolume'
        data = {"auth_token": 'YOUR_AUTH_TOKEN', 'value': detections}
        
        fullUrl = '%s/widgets/%s' % (url, widget)

        requests.post(fullUrl, data=json.dumps(data), headers=headers)

			
