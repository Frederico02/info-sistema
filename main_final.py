#********************* BGINFO_MULTI ***************************
#        Desenvolvido por Frederico de Jesus Almeida
#              Analista de Suporte PLENO - Multi
#*******************   06/06/2023  ****************************



import os
import re
import psutil
import socket
import subprocess
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
    # Obtém o nome de domínio do computador
    texto = socket.getfqdn()
    if "MLTBR.LOCAL" in texto:
        return ("Domínio: 'MLTBR.LOCAL'")
    else:
        return ("Domínio: NONE")


def update_data():
    # Atualiza os dados dos widgets da interface gráfica
    hostname_label.config(text='Hostname: ' + get_hostname())
    mac_address_label.config(text='MAC: ' + get_mac_address())
    ip_address_label.config(text='IP: ' + get_ip_address())
    username_label.config(text='Usuário : ' + get_username())
    domain_label.config(text=get_domain())

    network_type = get_network_type()
    network_type_label.config(text='' + network_type)

    # Aguarda 5 minutos e chama a função update_data novamente
    root.after(300000, update_data)

#Função que verifica se esta no wifi ou no cabo
def verificar_conectado(linha):
    padrao = r"\bConectado\b"
    resultado = re.search(padrao, linha)
    if resultado:
        return False
    else:
        return True

#Função que retorna o tipo da conexão
def get_network_type():

    # Chama a função no CMD
    output = subprocess.check_output('netsh interface show interface | findstr "Ethernet"', shell=True)

    # Decodifica a saída para uma string legível
    output = output.decode('utf-8')

    #Verifica se esta conectado no wi-fi ou no cabo
    if verificar_conectado(output):
        wifi = subprocess.check_output('netsh wlan show interfaces | findstr "Faixa"', shell=True)
        wifi = wifi.decode('utf-8')
        wifi = wifi.replace(" ", "")
        return (wifi)
    else:
        wifi = 'Conexão: Cabeada'
        return (wifi)


get_network_type()

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
window_height = 180
x_position = screen_width - window_width
y_position = screen_height - window_height
root.geometry('{}x{}+{}+{}'.format(window_width, window_height, x_position, y_position))

# Cria os widgets da interface
hostname_label = tk.Label(root, text='Hostname: ' + get_hostname(), anchor='w', justify='left')
mac_address_label = tk.Label(root, text='MAC: ' + get_mac_address(), anchor='w', justify='left')
ip_address_label = tk.Label(root, text='IP: ' + get_ip_address(), anchor='w', justify='left')
username_label = tk.Label(root, text='Usuário: ' + get_username(), anchor='w', justify='left')
domain_label = tk.Label(root, text=get_domain(), anchor='w', justify='left')
network_type_label = tk.Label(root, text='' + get_network_type(), anchor='w', justify='left')

# Posiciona os widgets na janela
hostname_label.pack()
mac_address_label.pack()
ip_address_label.pack()
username_label.pack()
domain_label.pack()
network_type_label.pack()

# Aguarda 5 minutos e chama a função update_data
root.after(30000, update_data)

# Inicia o loop da interface gráfica
root.mainloop()
