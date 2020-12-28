from socket import socket, AF_INET, SOCK_STREAM
def main():
    s=socket(AF_INET,SOCK_STREAM)
    print("TCP SOCKET PROGRAM : CLIENT  ")

    HEADERSIZE=10
    ip='192.168.0.107'
    port=1029
    s.connect((ip,port))
    print("Client Connected to the server ")
    request=input("Enter Filename : ")
    s.send(bytes(request,'utf-8'))
    print(f"Request for contents of File : {request} sent.")
    new_msg=True
    fullmsg=''
    while True:
        response=s.recv(50)
        response=response.decode('utf-8')
        if new_msg:
            msglen= int(response[:HEADERSIZE])
            new_msg=False
        fullmsg+=response
        if len(fullmsg)-HEADERSIZE == msglen :
            print("-"*10)
            print(f"Contents of file { request } : ")
            print(fullmsg[HEADERSIZE:])
            print("-"*10)
            print("Content Recieved.")
            s.close()
            print("Connection Terminated . ")
            break

main()