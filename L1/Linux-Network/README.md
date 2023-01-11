## Linux Networking. Home task

### 1.Based on VirtualBox create a network according the next scheme:

![](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/Linux-Network/png/Screenshot_1.png)

**Net1:** NAT 10.0.2.15
**Net2:** 10.75.18.0/24  
**Net3:** 10.1.75.0/24  
**Net4:** 172.16.18.0/24   

### Server_1:

**OS:** Ubuntu 22.04.1.LTS
**Int1:** 10.0.2.15
**Int2:** 10.75.18.1 (Static)
**Int3:** 10.1.75.1 (Static)

### DHCP Settings:

**IP range:**
10.75.18.11 - 10.75.18.29
10.1.75.10 - 10.1.75.30

![](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/Linux-Network/png/Screenshot_3.jpg)

### Client_1:

**OS:** CentOS LInux 7  
**Int1:** 10.75.18.12 (DHCP)  
**Int2:** 172.16.18.2 (Static)

### Client_2:

**OS:** Ubuntu 22.04.1.LTS  
**Int1:** 10.1.75.10 (DHCP)  
**Int2:** 172.16.18.1 (Static)

![](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/Linux-Network/png/Screenshot_2.jpg)

### 2. Check conections across the machines

![](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/Linux-Network/png/ping_check.jpg)

### task 4 routing

setup lo interface on Client_1
172.17.28.1/24
172.17.38.1/24

Setup routes to pass from Client_2 to 
172.17.28.1/24 through Server_1
172.17.38.1/24 through Net4

### task 5 summarizing

172.17.28.1
172.17.38.1


10101100.00010001.00 011100.00000001
10101100.00010001.00 100110.00000001

18
255.255.192.0

172.17.0.0/18

### task 6 SSH connections



