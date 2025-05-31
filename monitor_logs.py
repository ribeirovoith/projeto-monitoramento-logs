import csv
from datetime import datetime
import random

# Função que gera um IP aleatório para simular origem do evento
def gerar_ip():
    return f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"

# Função que gera um evento de login inválido com dados simulados
def gerar_evento_login_invalido():
    usuario = random.choice(['usuario1', 'usuario2', 'usuario3', 'admin', 'guest'])
    ip_origem = gerar_ip()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tipo_evento = "login_invalido"
    return [timestamp, usuario, tipo_evento, ip_origem]

# Função que grava o evento no arquivo CSV (append)
def gravar_evento_csv(evento, nome_arquivo='logs.csv'):
    # Verifica se o arquivo existe para saber se deve colocar o cabeçalho
    try:
        with open(nome_arquivo, 'r'):
            existe = True
    except FileNotFoundError:
        existe = False

    with open(nome_arquivo, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not existe:
            # Cabeçalho do CSV
            writer.writerow(['timestamp', 'usuario', 'tipo_evento', 'ip_origem'])
        writer.writerow(evento)

if __name__ == "__main__":
    evento = gerar_evento_login_invalido()
    gravar_evento_csv(evento)
    print(f"Evento registrado: {evento}")
