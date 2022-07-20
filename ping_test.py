import os
command = "ping -c 2"
ip = raw_input("Enter Ip Address:")
for i in range(1,256)
	iptest = ip + str(i)
	cmd = os.popen(command + " " + iptest)
	if "ttl" in cmd.read():
		print("IP:" , iptest)
	else:
		print("Not Ping:" , iptest)
		