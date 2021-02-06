Configuration de ADDC sur Virtualbox
<<<<<<<<<<<<<<<<<<<<<WORKING ENVIRONEMENT>>>>>>>>>>>>>>>>>>>>>
1.  [] Working env:
RAM: 16 GiB
OS: Ubuntu 20.04.1 LTS

<<<<<<<<<<<<<<<<<<<<<NETWORK & ADDS SETUP FOR UEH>>>>>>>>>>>>>>>>>>>>>
2.  [] Install Virtualbox
3.  [] Download Windows Server 2019 iso file at http://hyper-v-backup.backupchain.com/windows-server-2019-iso-free-download-hyper-v-server-2019/

4.  [] Create a VM with the iso in Virtualbox; name it Domain_Controller_Windows_Server_2019
5.  [] Password:Qwerty!123456789
6.  [] Isolate Domain_Controller_Windows_Server_2019 network:
>>> FilePpreferences/Network + add NatNetwork
7.  [] Give the DC a static IP: (info in ipconfig /all)
>>> IP: 10.0.2.100
>>> Subnetmask: 255.255.255.0
>>> Default GW: 10.0.2.1
>>> Prefered DNS server: 127.0.0.1
>>> Alternative DNS server: 8.8.8.8
8.  [] Enable the domain controller
>>> Manage/Add rows and features/Next/Next/Next + Check Acive Direcrory Domain Services + Add Features + Next/Next/Install
>>> Promote this server to a domain controller + check Add new forest
>>> Root domain name: ueh.edu
>>> DSRM password : Qwerty!123456789
>>> Next/Next/Next
>>> Resart
<<<<<<<<<<<<<<<<<<<<<SET UP USER VM>>>>>>>>>>>>>>>>>>>>>
9.  [] Start a new VM user_fds and ping the DC:
>>> ping 10.0.2.100
10. [] Force the  user_fds to use the DC DNS
>>> Prefered DNS server: 10.0.2.100
>>> Alternative DNS server: 8.8.8.8
>>> Control panel/System and Security/System + Change settings
>>> Change + check domain
<<<<<<<<<<<<<<<<<<<<<ADD A USER IN THE DOMAIN>>>>>>>>>>>>>>>>>>>>>
11. [] Add a user
>>> Tools/Active Directory users and computers/ueh.edu/users/New/User

<<<<<<<<<<<<<<<<<<<<<SOURCES>>>>>>>>>>>>>>>>>>>>>
https://www.youtube.com/watch?v=puIaRzZEwyY
https://www.youtube.com/watch?v=8GrblBtgul0
