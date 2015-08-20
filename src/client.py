# In The Name Of God
# ========================================
# [] File Name : client.py
#
# [] Creation Date : 19-08-2015
#
# [] Created By : Elahe Jalalpour (elahejalalpoor@gmail.com)
# =======================================
__author__ = 'Elahe Jalalpour'

import urllib.request
import urllib.parse
import http.client
import json
from collections import namedtuple


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
        req = urllib.request.Request(method=method, url=self.url_prefix + action)
        if body is not None:
            req.data = json.dumps(body)
            req.add_header('Content-Type', 'application/json')
        try:
            res = urllib.request.urlopen(req)
        except urllib.request.URLError:
            raise
        else:
            if res.status in (http.client.OK,
                              http.client.CREATED,
                              http.client.ACCEPTED,
                              http.client.NO_CONTENT):
                return res
            else:
                raise http.client.HTTPException(
                    res, 'code %d reason %s' % (res.status, res.reason),
                    res.getheaders(), res.read())

    def _do_request_body(self, method, action):
        """
        :type method: str
        :type action: str
        :rtype: object
        """
        res = self._do_request(method, action)
        return str(res.read(), 'ASCII')


class RyuClientFirewall(RyuClientBase):
    def __init__(self, address):
        super(RyuClientFirewall, self).__init__('firewall', address)

    def get_status(self):
        switches = []
        for obj in json.loads(self._do_request_body('GET', '/module/status')):
            switch = namedtuple('Switch', obj.keys())(*obj.values())
            switches.append(switch)
        return switches

    def set_enable(self, switchid):
        self._do_request('PUT', '/module/enable/{:0>16}'.format(switchid))

    def set_disable(self, switchid):
        self._do_request('PUT', '/module/disable/{:0>16}'.format(switchid))

    def get_log_status(self):
        logs = []
        for obj in json.loads(self._do_request_body('GET', '/log/status')):
            log = namedtuple('SwitchLog', obj.keys())(*obj.values())
            logs.append(log)
        return logs

    def set_log_enable(self, switchid):
        self._do_request('PUT', '/log/enable/{:0>16}'.format(switchid))

    def set_log_disable(self, switchid):
        self._do_request('PUT', '/log/disable/{:0>16}'.format(switchid))

    def get_rules(self, switchid):
        rules = []
        for obj in json.loads(self._do_request('GET', '/rules/{:0>16}'.format(switchid))):
            rule = namedtuple('Rule', obj.keys())(*obj.values)
            rules.append(rule)
        return rules
