from pickle import NONE
import subprocess
c1 = "netsh wlan show profiles"
v= "All User Profile"
file_pass = open('pass.txt', 'w')

a = subprocess.check_output(c1.split("")).decode('utf-8').split('\n')
a = [for i in a if "All User Profile" in i]
for i in a:
    try:
        t = i.split(':').replace('\r' , '')
        t = t.strip()
        result = subprocess.check_output(['netsh','wlan','show','profiles', t , 'key=clear']).decode('utf-8').split('\n')
        result = [b for b in result if "key content" in b]
        p = str(result).split("key content")[1].strip()
        file_pass.write(t+p+ '\n')
        print(t,p)
    except: 
        None

file_pass.close()