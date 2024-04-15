with open("roter1.txt","r") as file1:
    output1=file1.read().splitlines()
temp1={}
for i in output1:
    temp1[i.split(':')[0]]=i.split(':')[1]

with open("router2.txt","r")as file2:
    output2=file2.read().splitlines()
temp2={}
for a in output2:
    temp2[a.split(':')[0]]=a.split(':')[1]
with open('router3.txt','r')as file3:
 output3=file3.read().splitlines()
 temp3={}
for b in output3:
    temp3[b.split(':')[0]]=b.split(':')[1]

from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("."))
temp= env.get_template("conf.j2")
result1= temp.render(asm=temp1)
with open('r1_conf.txt','w')as conf:
    conf.write(result1)
result2= temp.render(asm=temp2)
with open('r2.conf1.txt','w')as conf2:
    conf2.write(result2)
result3= temp.render(asm=temp3)
with open('r3.conf3.txt','w')as conf3:
    conf3.write(result3)
import paramiko
import time
from datetime import datetime
import getpass
pass1 =getpass.getpass('Enter asem password : ')
pass2 =getpass.getpass('Enter asem1 password : ')
pass3 = getpass.getpass('Enter asem2 password : ')
date = datetime.now()
ssh = paramiko .SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
router=[{'hostname':'192.168.110.142','port':22,'username':'asem','password':pass1},{'hostname':'192.168.110.143','port':22,'username':'asem1','password':pass2},{'hostname':'192.168.110.144','port':22,'username':'asem2','password':pass3}]
for r in router:
    ssh.connect(**r,look_for_keys= False,allow_agent=False)
    if r['hostname']=='192.168.110.142':
        cli = ssh.invoke_shell()
        cli.send ('en \n')
        cli.send('terminal length 0 \n')
        cli.send("conf t \n")
        with open('r1_conf.txt','r') as f1:
            out=f1.readlines()
        for o in out:
            cli.send(o)
        cli.send('end \n')
        cli.send('show bgp summary \n')
        time.sleep(3)
        output=cli.recv(99999).decode()
        with open(str(date.date())+'r1','w')as v1:
            v1.write(output)
    elif r['hostname'] == '192.168.110.143':
        cli = ssh.invoke_shell()
        cli.send('en \n')
        cli.send('terminal length 0 \n')
        cli.send("conf t \n")
        with open('r2.conf1.txt','r') as jj:
            out1=jj.readlines()

    else:
        cli = ssh.invoke_shell()
        cli.send('en \n')
        cli.send('terminal length 0 \n')
        cli.send("conf t \n")
        with open('r3.conf3.txt', 'r') as gg:
            out2 = gg.readlines()
        for ff in out2:
            cli.send(ff)
        cli.send('end \n')
        cli.send('show bgp summary \n')
        time.sleep(3)
        output3 = cli.recv(99999).decode()
        with open(str(date.date()) + 'r3', 'w') as v3:
            v3.write(output3)
print("the change committed")
print("new test cases")
print("this is changes")
