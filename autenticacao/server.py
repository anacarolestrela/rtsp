import socket

# Dicionário de usuários e senhas
users = {
    "usuario1": "senha1",
    "usuario2": "senha2"
}

# Função para autenticar o usuário
def autenticar_usuario(username, password):
    return username in users and users[username] == password

# Configuração do servidor
host = '127.0.0.1'  # Endereço IP local
port = 12345  # Porta arbitrária

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)  # Até 1 cliente por vez
print(f"Servidor esperando por conexões em {host}:{port}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Conexão estabelecida com {client_address}")

    username = client_socket.recv(1024).decode('utf-8')
    password = client_socket.recv(1024).decode('utf-8')

    if autenticar_usuario(username, password):
        client_socket.send("Autenticação bem-sucedida".encode('utf-8'))

    else:
        client_socket.send("Falha na autenticação".encode('utf-8'))

    client_socket.close()
