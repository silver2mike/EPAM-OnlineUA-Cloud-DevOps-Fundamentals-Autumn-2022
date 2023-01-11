## Linux Networking. Home task

### 1. Based on VirtualBox create a network according the next scheme:

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

### 2. DHCP Settings:

**IP ranges:**  
10.75.18.11 - 10.75.18.20  
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

### 3. Check conections across the machines

![](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/Linux-Network/png/ping_check.jpg)

### 4. Routing

**setup lo interface on Client_1**  
172.17.28.1/24  
172.17.38.1/24  

![](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/Linux-Network/png/task41.jpg)

**Setup routes to pass from Client_2 to**   
172.17.28.1/24 through Server_1  
172.17.38.1/24 through Net4  

**Server_1**  
sudo ip route add 172.17.28.1 via 10.1.75.1  
![](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/Linux-Network/png/task4serv.jpg)

**Client_2**  
sudo ip route add 172.17.28.1 via 10.1.75.1  
sudo ip route add 172.17.38.1 via 172.16.18.2  
![](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/Linux-Network/png/task4cl2.jpg)

### 5. Summarizing
Calculate common IP address and netmask for  
172.17.28.1  
172.17.38.1  

10101100.00010001.00|011100.00000001  
10101100.00010001.00|100110.00000001  

First 18 bits are the same so netmask is /18   
or  
255.255.192.0  

Summarized addres is **172.17.0.0/18**  

**Server_1**  
sudo ip route add 172.17.0.0/18 via 10.75.18.12   
![](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/Linux-Network/png/task5serv.jpg)

**Client_2**  
sudo ip route add 172.17.0.0/18 via 10.1.75.1  
![](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/Linux-Network/png/task5cl2.jpg)

### 6. SSH connections

Setup SSH connections between Server and Clients and both Clients  

**Server_1**  
![](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/Linux-Network/png/ssh-server.jpg)

**Client_1**  
![](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/Linux-Network/png/ssh-c1-server.jpg)
![](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/Linux-Network/png/ssh-c1-c2.jpg)

**Client_2**  
![](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/Linux-Network/png/ssh-c2.jpg)

### 7. Iptables  
Setup Server_1 Firewall for:  
- Allow SSH connection from Client_1 and Deny SSH connection from Client_2  
![](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/Linux-Network/png/task61.jpg)
![](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/Linux-Network/png/task6.jpg)

- Allow ping from Client_2 to 172.17.28.1. Deny ping from Client_2 to 172.17.38.1
![](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/Linux-Network/png/task62.jpg)

### 8. NAT translation 
Setup Iptables with NAT translation to give access to the Internet from Clients

sudo iptables -t nat -A POSTROUTING -o enp0s3 -j MASQUERADE

![](https://github.com/silver2mike/EPAM-OnlineUA-Cloud-DevOps-Fundamentals-Autumn-2022/blob/main/L1/Linux-Network/png/task8.jpg)

