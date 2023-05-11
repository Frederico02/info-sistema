#/*            Info sistemas windowns             */
#/*		          Gupo Multi 10/05/2023           */
#/*	    Frederico Almeida - Analista de Suporte PL */

import os
import psutil
import socket
import tkinter as tk

def get_ip_address():
    ip_local = socket.gethostbyname(socket.gethostname())
    return ip_local

def get_mac_address():
    # Obtém o endereço MAC do adaptador de rede principal
    mac_address = ''
    for iface in psutil.net_if_addrs().values():
        for addr in iface:
            if addr.family == psutil.AF_LINK:
                mac_address = addr.address
                break
        if mac_address:
            break
    return mac_address

def get_hostname():
    # Obtém o nome do host do computador
    return socket.gethostname()

def get_username():
    # Obtém o nome do usuário logado
    return os.getlogin()

def get_domain():
    # Obtém o nome de domínio totalmente qualificado do computador
    texto = socket.getfqdn()
    if "MLTBR.LOCAL" in texto:
        return("Domínio: 'MLTBR.LOCAL'")
    else:
        return("Domínio: NONE")

def update_data():
    # Atualiza os dados dos widgets da interface gráfica
    hostname_label.config(text='Hostname: ' + get_hostname())
    mac_address_label.config(text='Endereço MAC: ' + get_mac_address())
    ip_address_label.config(text='Endereço IP: ' + get_ip_address())
    username_label.config(text='Usuário logado: ' + get_username())
    domain_label.config(text=get_domain())

    # Aguarda 5 minutos e chama a função update_data novamente
    root.after(300000, update_data)

# Cria a janela principal
root = tk.Tk()
root.title('Sistema')

# Configura o fundo da janela para ser transparente
root.attributes('-alpha', 0.5)

# Oculta a barra de título
root.overrideredirect(True)

# Define a posição da janela no canto inferior direito
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 300
window_height = 150
x_position = screen_width - window_width
y_position = screen_height - window_height
root.geometry('{}x{}+{}+{}'.format(window_width, window_height, x_position, y_position))

# Cria os widgets da interface
hostname_label = tk.Label(root, text='Hostname: ' + get_hostname())
mac_address_label = tk.Label(root, text='Endereço MAC: ' + get_mac_address())
ip_address_label = tk.Label(root, text='Endereço IP: ' + get_ip_address())
username_label = tk.Label(root, text='Usuário logado: ' + get_username())
domain_label = tk.Label(root, text=get_domain())

# Posiciona os widgets na janela
hostname_label.pack()
mac_address_label.pack()
ip_address_label.pack()
username_label.pack()
domain_label.pack()

# Aguarda 5 minutos e chama a função update_data
root.after(300000, update_data)

# Inicia o loop da interface gráfica
root.mainloop()
