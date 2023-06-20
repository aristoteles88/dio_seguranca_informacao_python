import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Socket criado com sucesso!")

host = 'localhost'
port = 5433
message = 'Olá servidor! Tudo bem?'


try:
    print(f"Cliente: {message}")
    s.sendto(message.encode(), (host, port))

    data, server = s.recvfrom(4096)
    data = data.decode()

    print(f"Cliente: {data}")
finally:
    print("Cliente: Fechando a conexão.")
    s.close()
