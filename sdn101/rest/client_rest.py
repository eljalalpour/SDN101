# In The Name Of God
# ========================================
# [] File Name : client_rest.py
#
# [] Creation Date : 19-08-2015
#
# [] Created By : Elahe Jalalpour (el.jalalpour@gmail.com)
# =======================================
__author__ = 'Elahe Jalalpour'

import urllib.request
import urllib.parse
import http.client
import json


class RyuClientBase:
    def __init__(self, module, address):
        self.module = module
        self.url_prefix = 'http://' + address + '/' + self.module

    def _do_request(self, method, action, body=None):
        """
        :type action: str
        :type method: str
        :rtype: http.client.Response
        """
        req = urllib.request.Request(method=method,
                                     url=self.url_prefix + action)
        if body is not None:
            req.data = json.dumps(body).encode('ASCII')
            req.add_header('Content-Type', 'application/json')
        try:
            res = urllib.request.urlopen(req)
        except urllib.request.HTTPError as res:
            print('code %d reason %s' % (res.code, res.reason))
            print(res.headers)
            print(str(res.read(), 'ASCII'))
        else:
            if res.status in (http.client.OK,
                              http.client.CREATED,
                              http.client.ACCEPTED,
                              http.client.NO_CONTENT):
                return res

    def _do_request_body(self, method, action, body=None):
        """
        :type method: str
        :type action: str
        :rtype: object
        """
        res = self._do_request(method, action, body)
        if res is not None:
            return str(res.read(), 'ASCII')
