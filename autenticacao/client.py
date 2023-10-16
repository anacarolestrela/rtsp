import tkinter as tk
import socket

# Função para lidar com a autenticação
def autenticar():
    username = entry_username.get()
    password = entry_password.get()

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    client_socket.send(username.encode('utf-8'))
    client_socket.send(password.encode('utf-8'))

    response = client_socket.recv(1024).decode('utf-8')

    client_socket.close()

    if response == "Autenticação bem-sucedida":
        label_result.config(text="Autenticação bem-sucedida")
        root.after(100, root.withdraw)  # Oculta a janela após a autenticação bem-sucedida
    else:
        label_result.config(text="Falha na autenticação")

# Configuração do cliente
host = '127.0.0.1'  # Endereço IP do servidor
port = 12345  # Porta do servidor

# Cria a janela principal
root = tk.Tk()
root.title("Autenticação de Usuário")

# Widgets
label_username = tk.Label(root, text="Nome de Usuário:")
label_password = tk.Label(root, text="Senha:")
entry_username = tk.Entry(root)
entry_password = tk.Entry(root, show="*")  # Use show="*" para ocultar a senha
button_login = tk.Button(root, text="Login", command=autenticar)
label_result = tk.Label(root, text="")

# Layout dos widgets
label_username.pack()
entry_username.pack()
label_password.pack()
entry_password.pack()
button_login.pack()
label_result.pack()

# Inicializa a janela
root.mainloop()
