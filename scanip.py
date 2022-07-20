from socket import *
ip=input("Enter The Ip:");
print("\n") 
n=0
for i in range(1,256):
	try:
		live=gethostbyaddr(ip + str(i)) #192.168.1.i
		print ("Ip Live:" + ip + str(i), " " + live[0])
	except:
		n+=1
		if n==2:
			breck;
		print( "-----------------")	
		
	