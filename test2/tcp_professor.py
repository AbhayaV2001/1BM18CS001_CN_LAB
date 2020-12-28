from socket import socket, AF_INET, SOCK_STREAM

def main():
    s=socket(AF_INET,SOCK_STREAM)
    print("TCP SOCKET PROGRAM : SERVER ")

    HEADERSIZE=10
    ip='192.168.0.107'
    port=1029
    s.bind((ip,port))  
    s.listen(4)

    print(f"Server is Up , Listening at Port : { port } ")

    while True:
        clientsocket, clientaddr= s.accept()
        print(f" Client with  {clientaddr} connected.")
        request=clientsocket.recv(1024)
        request=request.decode('utf-8')
        print(f"Request for filecontent of file : { request } Recieved. ")
        try:
            with open(request,"r") as fd:
                contents=fd.read()
                print("Request Processed")
        except:
            contents="Request cannot be fullfilled. No file exist."
            print("Request cannot be fullfilled")
        # Data send == {len ...+ contents }
        msg=f"{len(contents):<{HEADERSIZE}}"+contents
        clientsocket.send(bytes(msg,'utf-8'))
        print(f"Response Sent to { clientaddr }")
        print("-"*10)

main()