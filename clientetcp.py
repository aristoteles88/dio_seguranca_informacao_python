import socket
import sys


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexão falhou!!!")
        print(f"Erro: {e}")
        sys.exit()

    print("Socket criado com sucesso!")

    target_host = input("Digite o IP ou Host a ser conectado: ")
    target_port = input("Digite a porta a ser conectada: ")

    try:
        s.connect((target_host,int(target_port)))
        print(f"Cliente TCP conectado com sucesso no host: {target_host} e na porta: {target_port}")
        s.shutdown(2)
    except socket.error as e:
        print(f"Não foi possível conectar no host: {target_host} - porta: {target_port} ")
        print(f"Erro: {e}")
        sys.exit()


if __name__ == "__main__":
    main()
