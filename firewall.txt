# Clear old rules and set defaults
iptables -P INPUT ACCEPT
iptables -P OUTPUT ACCEPT
iptables -P FORWARD ACCEPT
iptables -F INPUT
iptables -F OUTPUT
iptables -F FORWARD
iptables -F -t nat
iptables -F -t mangle

# Local and trusted hosts and networks
iptables -A INPUT -i lo -j ACCEPT
iptables -A INPUT -s 192.168.0.0/24 -j ACCEPT # example how to allow whole IP network 192.168.0.xxx
iptables -A INPUT -s 193.167.100.97 -j ACCEPT # DO NOT COMMENT OR MODIFY THIS. THIS IS BACKDOOR TO YOUR SERVER FROM students.oamk.fi
#iptables -A INPUT -p icmp -j REJECT
iptables -A INPUT -p icmp -j ACCEPT
# Completely open services
iptables -A INPUT -p tcp --dport 22 -j ACCEPT # DO NOT COMMENT OR MODIFY THIS. YOU WILL KICK YOURSELF OUT FROM THE SERVER (SSH)
iptables -A INPUT -p tcp --dport 80 -j ACCEPT # HTTP
