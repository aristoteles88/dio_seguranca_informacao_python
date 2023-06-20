import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Socket criado com sucesso!")

host = 'localhost'
port = 5433
message = '\nCliente: Olá servidor! Tudo bem?'


try:
    print(f"\nCliente: {message}")
    s.sendto(message.encode(), (host, 5432))

    data, server = s.recvfrom(4096)
    data = data.decode()

    print(f"\nCliente: {data}")
finally:
    print("\nCliente: Fechando a conexão.")
    s.close()
