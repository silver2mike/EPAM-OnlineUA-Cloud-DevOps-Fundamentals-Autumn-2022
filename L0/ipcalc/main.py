# Ip calculator
#

netmask_prefix = 24

netmask_bin = ""           # Binary netmask string
netmask_bin_split = []     # Binary netmask list split by octets 
netmask_dec_split = []     # Decimal netmask list split by octets 

net_len = 0

i = 0

custom_ip = "10.20.30.40"
custom_ip_bin = ""           # Binary netmask string
custom_ip_bin_splitted = []  # Binary IP list split by octets

# Netmask transform

while len(netmask_bin) < netmask_prefix:
    netmask_bin += "1"

while len(netmask_bin) < 32:
    netmask_bin += "0"
    net_len += 1

# create binary netmask splitted
netmask_bin_split.append(netmask_bin[0:8])
netmask_bin_split.append(netmask_bin[8:16])
netmask_bin_split.append(netmask_bin[16:24])
netmask_bin_split.append(netmask_bin[24:32])

# create decimal netmask splitted
netmask_dec_split.append(str(int(netmask_bin_split[0], 2)))
netmask_dec_split.append(str(int(netmask_bin_split[1], 2)))
netmask_dec_split.append(str(int(netmask_bin_split[2], 2)))
netmask_dec_split.append(str(int(netmask_bin_split[3], 2)))

print("Netmask prefix :" + str(netmask_prefix))
# print("Binary  netmask:  " + netmask_bin)
print("Binary  netmask:  " + netmask_bin[0:8]+"."+netmask_bin[8:16]+"."+netmask_bin[16:24]+"."+netmask_bin[24:32])

print("Decimal netmask:  " + netmask_dec_split[0] + "." + netmask_dec_split[1] + "." + netmask_dec_split[2]
      + "." + netmask_dec_split[3])

print("Network length :  " + str(net_len))
print("========================================")

# IP dec to bin transform
# --------------------------------------------------------------------------------------------------
# create binary IP splitted
s = custom_ip.split(".")
# print(s)
while len(custom_ip_bin_splitted) < len(s):
    i = len(custom_ip_bin_splitted)
    custom_ip_bin_splitted.append(str(bin(int(s[i]))[2:]))

    custom_ip_bin_splitted[i] = custom_ip_bin_splitted[i].rjust(8, '0')
    custom_ip_bin += custom_ip_bin_splitted[i]


print("IP address       : " + custom_ip)
# print("IP address in Bin: " + custom_ip_bin)
print("IP address in Bin: " + custom_ip_bin_splitted[0] + "." + custom_ip_bin_splitted[1] + "." +
      custom_ip_bin_splitted[2] + "." + custom_ip_bin_splitted[3])

network_addr = int(custom_ip_bin, 2) & int(netmask_bin, 2)

network_addr_bin = str(bin(int(network_addr))[2:])
network_addr_bin = network_addr_bin.rjust(32, '0')

network_addr_dec = str(int(network_addr_bin[0:8], 2)) + "." + str(int(network_addr_bin[8:16], 2)) + "." + \
                   str(int(network_addr_bin[16:24], 2)) + "." + str(int(network_addr_bin[24:32], 2))

# print(custom_ip_bin)
# print(netmask_bin)
print("Network address in Bin: " + str(network_addr_bin[0:8]) + "." + str(network_addr_bin[8:16]) + "." +
      str(network_addr_bin[16:24]) + "." + str(network_addr_bin[24:32]))
print("Network address in Dec: " + network_addr_dec)
