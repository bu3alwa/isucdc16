#!/bin/sh
iptables --policy INPUT ACCEPT
iptables --policy OUTPUT ACCEPT

iptables --flush INPUT
iptables --flush OUTPUT
