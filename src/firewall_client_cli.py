# In The Name Of God
# ========================================
# [] File Name : firewall_client_cli.py
#
# [] Creation Date : 20-08-2015
#
# [] Created By : Elahe Jalalpour (el.jalalpour@gmail.com)
# =======================================
__author__ = 'Elahe Jalalpour'

import cmd
from client_rest import RyuClientFirewall

try:
    import termcolor
except ImportError:
    termcolor = None


class FirewallCLICmd(cmd.Cmd):
    def __init__(self):
        super(FirewallCLICmd, self).__init__()
        self.firewall = None
        self.intro = """
{0:*^160}
{1:=^160}
Firewall CLI Application version 0.9, Copyright (C) 2015 Elahe Jalalpour (elahejalalpoor@gmail.com)
Renamer comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
This is free software, and you are welcome to redistribute it
under certain conditions; type `show c' for details.
""".format("Welcome", " CLI program for using ryu based firewall application which is written by Elahe Jalalpour ")

    def preloop(self):
        prompt = "Firewall CLI []"
        if termcolor:
            prompt = termcolor.colored(prompt, color="red", attrs=['bold'])
        server = input("{} Please enter firewall ip address: ".format(prompt))
        port = input("{} Please enter firewall port: ".format(prompt))
        self.firewall = RyuClientFirewall("{0}:{1}".format(server, port))

    def do_get_status(self, line):
        switches = self.firewall.get_status()
        for switch in switches:
            print("{:#^80}".format(''))
            print("Switch ID: {}".format(switch.switch_id))
            print("Status: {}".format(switch.status))
            print("{:#^80}".format(''))

    def do_set_enable(self, line):
        try:
            switchid = int(line)
        except ValueError as e:
            print("*** Invalid number: {}".format(str(e)))
        else:
            self.firewall.set_enable(switchid)

    def do_set_disable(self, line):
        try:
            switchid = int(line)
        except ValueError as e:
            print("*** Invalid number: {}".format(str(e)))
        else:
            self.firewall.set_disable(switchid)

    def do_get_log_status(self):
        pass

    def do_set_log_enable(self, switchid):
        pass

    def do_set_log_disable(self, switchid):
        pass

    def do_get_rules(self, line):
        try:
            switchid = int(line)
        except ValueError as e:
            print("*** Invalid number: {}".format(str(e)))
        else:
            rules = self.firewall.get_rules(switchid)
            for rule in rules:
                print("{:#^80}".format(''))
                for key, value in rule.items():
                    print("{0}: {1}".format(key, value))
                print("{:#^80}".format(''))

    def do_get_vlan_rules(self, switchid, vlanid):
        pass

    def do_set_rule(self, line):
        rule = {}
        try:
            switchid = int(line)
        except ValueError as e:
            print("*** Invalid number: {}".format(str(e)))
        else:
            fields = [('priority', '<0 to 65533>'), ('in_port', '<int>'), ('dl_src', '<xx:xx:xx:xx:xx:xx>'),
                      ('dl_dst', '<xx:xx:xx:xx:xx:xx>'), ('dl_type', '<ARP or IPv4 or IPv6>'),
                      ('nw_src', '<A.B.C.D/M>'),
                      ('nw_dst', '<A.B.C.D/M>'),
                      ('ipv6_src', '<xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/M>'),
                      ('ipv6_dst', '<xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/M>'),
                      ('nw_proto', '<TCP or UDP or ICMP or ICMPv6>'),
                      ('tp_src', '<int>'),
                      ('tp_dst', '<int>'),
                      ('actions', '<ALLOW or DENY>')]
            for key, desc in fields:
                value = input("{0} ({1}): ".format(key, desc))
                if value != '':
                    rule[key] = value
            print(self.firewall.set_rule(rule, switchid))

    def do_set_vlan_rule(self, rule, switchid, vlanid):
        pass

    def do_delete_rule(self, line):
        try:
            switchid = int(line.split(' ')[0])
            ruleid = int(line.split(' ')[1])
        except ValueError as e:
            print("*** Invalid number: {}".format(str(e)))
        else:
            print(self.firewall.delete_rule({'rule_id': ruleid}, switchid))

    def do_delete_vlan_rule(self, rule, switchid, vlanid):
        pass

    @property
    def prompt(self):
        switches_no = len(self.firewall.get_status())
        prompt = "Firewall CLI [{} online switch] > ".format(switches_no)
        if termcolor:
            prompt = termcolor.colored(prompt, color="red", attrs=['bold'])
        return prompt

    def do_quit(self, line):
        print("Thank you for using Firewall CLI")
        return True

    do_EOF = do_quit


FirewallCLICmd().cmdloop()
