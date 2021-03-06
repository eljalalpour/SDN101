# In The Name Of God
# ========================================
# [] File Name : client_rest.py
#
# [] Creation Date : 19-08-2015
#
# [] Created By : Elahe Jalalpour (el.jalalpour@gmail.com)
# =======================================
__author__ = 'Elahe Jalalpour'

import json
from collections import namedtuple

from rest.client_rest import RyuClientBase


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
        objs = json.loads(self._do_request_body('GET', '/rules/{:0>16}'.format(switchid)))
        if len(objs[0]['access_control_list']) > 0:
            for obj in objs[0]['access_control_list'][0]['rules']:
                rules.append(obj)
        return rules

    def get_vlan_rules(self, switchid, vlanid):
        rules = []
        for obj in json.loads(self._do_request_body('GET', '/rules/{0:0>16}/{1}'.format(switchid, vlanid))):
            rule = namedtuple('Rule', obj.keys())(*obj.values)
            rules.append(rule)
        return rules

    def set_rule(self, rule, switchid):
        return self._do_request_body('POST', '/rules/{:0>16}'.format(switchid), rule)

    def set_vlan_rule(self, rule, switchid, vlanid):
        return self._do_request_body('POST', '/rules/{0:0>16}/{1}'.format(switchid, vlanid), rule)

    def delete_rule(self, rule, switchid):
        return self._do_request_body('DELETE', '/rules/{:0>16}'.format(switchid), rule)

    def delete_vlan_rule(self, rule, switchid, vlanid):
        return self._do_request_body('DELETE', '/rules/{0:0>16}/{1}'.format(switchid, vlanid), rule)
