#Server 
import socket, pickle 
from arquivo import Arquivo

def indexar_arquivo(arquivo):
   pass
   

def pesquisar_palavras_chave(palavras_chave):
    return "Resultados da pesquisa aqui"


def programa_servidor():
    #Função para executar o Servidor 

    host = socket.gethostname()
    porta = 5000

    socket_servidor = socket.socket()
    socket_servidor.bind((host, porta))

    socket_servidor.listen(2)
    conexao, endereco = socket_servidor.accept()

    print("Conexão efetuada com sucesso do endereço: " + str(endereco))

    while True:
        dados = conexao.recv(4096)

        if not dados:
            break

        if isinstance(dados, Arquivo):
            arquivo = pickle.loads(dados)
            indexar_arquivo(arquivo)
            print("Arquivo indexado:", arquivo.nome)
            conexao.send("Arquivo recebido e indexado com sucesso!".encode())
        else:
            resposta = pesquisar_palavras_chave(dados.decode())
            conexao.send(resposta.encode())

    conexao.close()

if __name__ == '__main__':
    programa_servidor()
