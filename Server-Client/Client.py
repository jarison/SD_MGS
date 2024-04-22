#Cliente
import socket, pickle
from arquivo import Arquivo

def fazer_upload_arquivo(socket_cliente):
    caminho_arquivo = input("Digite o caminho do arquivo a ser enviado: ")
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            nome_arquivo = input("Digite o nome do arquivo: ")
            arquivo = arquivo(nome_arquivo, conteudo)
            socket_cliente.send(pickle.dumps(arquivo))
            print("Arquivo enviado com sucesso!")
    except FileNotFoundError:
        print("Arquivo não encontrado.")

def fazer_pesquisa(socket_cliente):
    palavras_chave = input("Digite as palavras-chave para pesquisa: ")
    socket_cliente.send(palavras_chave.encode())
    resposta = socket_cliente.recv(4096)
    print(resposta.decode())

def programa_cliente():
    #Função para executar o Client

    host = socket.gethostname()
    porta = 5000

    socket_cliente = socket.socket()
    socket_cliente.connect((host, porta))

    while True:
        print("1. Fazer upload de arquivo")
        print("2. Fazer pesquisa de palavras-chave")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            fazer_upload_arquivo(socket_cliente)
        elif opcao == '2':
            fazer_pesquisa(socket_cliente)
        else:
            break

    socket_cliente.close()

if __name__ == '__main__':
    programa_cliente()
