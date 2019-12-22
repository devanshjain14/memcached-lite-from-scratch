#import socket
#
#IP = "127.0.0.1"
#PORT = 6969
#
#client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client_socket.connect((IP, PORT))
#client_socket.sendall(bytes("Client Socket",'UTF-8'))
#
#while True:
#
#    smsg =  client_socket.recv(1024)
#    print(smsg.decode())
#
#    cmsg1 = input()
#    send_od=(cmsg1.lower()).split()
#    if send_od[0]=='set' :
#        if len(send_od)==3:
#            cmsg2 = input()
#            cmsg1=cmsg1+ " " + cmsg2
#        else:
#            print('')
#
#    client_socket.sendall(bytes(cmsg1,'UTF-8'))
#    if cmsg1=='exit':
#        break
#
#client_socket.close()


