import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Socket criado com sucesso!!")

host = 'localhost'
port = 5432


s.bind((host, port))

message = "\nServidor: Olá Cliente! Tranquilo, e você?"

while 1:
    data, addr = s.recvfrom(4096)

    if data:
        print("\nServidor enviando mensagem...")
        s.sendto(data + message.encode(), addr)
