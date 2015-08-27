=======
SDN 101
=======
Introduction
------------
Customizable network idea has been recently given a significant acceleration in the emergence of SDN.
it, often focuses on the main new idea programmable network.
SDN guarantees to significantly ease network management and network programming capability also uses the possibility
of implementing new ideas to create the network.

Project
-------
As a project we implemented simple firewall with python on `ELRyu Controller`_,
and for testing it we used `mininet platform`_.

I personally prefer python3 so I ported `Ryu Controller`_ on python3 and named it `ELRyu Controller`_

Usage's Sample
..............
1. Run firewall application on ryu with following command:
::
    $ ryu-manager sdn101/app/rest_firewall.py

2. Run mininet with your custom options using command that like following command:
::
    $ sudo mn --switch=ovs,protocol=OpenFlow13 --controller=remote,x.x.x.x

3. Run firewall client application with following command:
::
    $ python3 sdn101/firewall_client_cli.py

4. enter your server ip address and port


Documentation
-------------
A Persian documentation about SDN and it's history can be found in `Introduction to SDN`_ on my google drive.



.. _ELRyu Controller: https://github.com/elahejalalpour/ELRyu
.. _mininet platform: http://mininet.org/
.. _Introduction to SDN: https://docs.google.com/document/d/1ViS_8O3iC8ExZQHhwPMEqcHDuvHJ4gotTIst0r7YYg0/edit?usp=sharing
.. _Ryu Controller: https://github.com/osrg/ryu