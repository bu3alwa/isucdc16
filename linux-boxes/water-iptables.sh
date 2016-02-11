#!/bin/sh
iptables -P INPUT DROP
iptables -P OUTPUT DROP
iptables -A INPUT -i lo -j ACCEPT
iptables -A OUTPUT -o lo -j ACCEPT
iptables -A INPUT -i eth1 -j ACCEPT
iptables -A OUTPUT -o eth1 -j ACCEPT
iptables -A INPUT -m state --state ESTABLISHED,RELATED -i eth0 -j ACCEPT
#iptables -A OUTPUT -o eth0 -j ACCEPT
iptables -A INPUT -i eth0 --source 192.168.1.4/32 --protocol tcp --destination-port 8001 -j ACCEPT
iptables -A OUTPUT -o eth0 --protocol tcp --source-port 8001 --destination 192.168.1.4/32 -j ACCEPT
iptables -A INPUT -i eth0 --source 192.168.1.7/32 --protocol tcp --destination-port 8001 -j ACCEPT
iptables -A OUTPUT -o eth0 --protocol tcp --source-port 8001 --destination 192.168.1.7/32 -j ACCEPT

# allow SSH if necessary
#iptables -A INPUT -i eth0 --source x.x.x.x/x --protocol tcp --destination-port 22 -j ACCEPT
#iptables -A OUTPUT -o eth0 --protocol tcp --destination x.x.x.x/x -j ACCEPT
