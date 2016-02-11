#!/bin/bash
iptables -P INPUT DROP
iptables -P OUTPUT DROP
iptables -A INPUT -i lo -j ACCEPT
iptables -A OUTPUT -o lo -j ACCEPT
iptables -A INTPUT -i eth1 -j ACCEPT
iptables -A OUTPUT -o eth1 -j ACCEPT
iptables -A INPUT -m state --state ESTABLISHED,RELATED -i eth0 -j ACCEPT
#iptables -A OUTPUT -o eth0 -j ACCEPT
iptables -A INPUT -i eth0 --source 192.168.1.7/32 --protocol tcp --destination-port 8000 -j ACCEPT
iptables -A OUTPUT -o eth0 --protocol tcp --source-port 8000 --destination 192.168.1.7/32 -j ACCEPT
iptables -A INPUT -i eth0 --source 192.168.5.1/32 --protocol tcp --destination-port 22 -j ACCEPT
iptables -A OUTPUT -o eth0 --protocol tcp --source-port 22 --destination 192.168.5.1/32 -j ACCEPT
