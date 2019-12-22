import socket
import threading
import csv
import io
from collections import defaultdict

hostname = socket.gethostname()    
IP = socket.gethostbyname(hostname)    
print("Your Computer Name is:" + hostname)    
print("Your Computer IP Address is:" + IP) 
# IP = "127.0.0.1"
PORT =6969
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((IP, PORT))

print("SERVER IS READY TO LISTEN ON")

class key_value_dict(dict):  
    def __init__(self):  
        self = dict()  
    def add(self, key, value):  
        self.setdefault(key, []).append(value)

my_dict = defaultdict(list)       
class ClientThread(threading.Thread):

    def __init__(self,caddr,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("Connection ", caddr)
        
    def run(self):
        command = ''
        
        while True:
            data = self.csocket.recv(2048)
            command = data.decode()
            msg=(command.lower()).split()
            dict_obj=key_value_dict()
            
            if msg[0]=='set':
                if len(msg)<4:
                    command='INVALID COMMAND'
                else:
                    key, length, value= msg[1], msg[2], msg[3]
                    lent=int(length)
                    dict_obj.add(key, value)
                    if len(msg[3])<lent:
                        with open('dict.csv', 'a') as f:
                            writer = csv.writer(f)
                            for key, value in dict_obj.items():
                                writer.writerow([key]+ value)                        
                            command='STORED'
                    else:
                        command='NOT STORED'

            elif msg[0]=='get':
                if 2==len(msg):
                    key = msg[1]
                    # with io.open('dict.csv', 'r', newline='', encoding='utf-8') as f:
                    #     val = dict(csv.reader(f)) 
                    # valid= (val[key])
                    with open('dict.csv', 'r') as csv_file:
                        csv_reader = csv.DictReader(csv_file)
                        for line in csv_reader:
                            for key, value in line.items():
                                my_dict[key].append(value)
                                for val in my_dict.values():
                                    if val == key:
                                        valid= value
                    if None != valid:
                        command= (key.upper() + ' ' +valid.upper() + "\nEND\n")
                    else:
                        command= 'NOT FOUND'
                else:
                    command='INVALID COMMAND'

            if command=='exit':
                break
            
            print ("CLIENT", command)
            self.csocket.send(bytes(command,'UTF-8'))
        print ("DISCONNECTED...")



while True:
    server_socket.listen(1)
    clientsock, caddr = server_socket.accept()
    newthread = ClientThread(caddr, clientsock)
    newthread.start()
