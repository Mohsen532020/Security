from socket import *
ip=input("Enter The Ip:");
print
ports=[13,21,22,23,53,80,135,139,445,443,3389]
for i in ports:
      sock=socket(AF_INET, SOCK_STREAM)
	  sock.settimeout(1)
	  r=sock.connect_ex((ip,i))
	  if r = 0:
	      print "Open:" ,i," " ",getservbyport(i)	  