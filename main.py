import random
import threading
from conta import conta
from transferencia import transferencia


def criar_contas(num_contas):
    contas = []
    for i in range(num_contas):
        saldo_inicial = round(random.uniform(1000, 5000), 2)  # Saldo inicial aleatório entre 1000 e 5000 com 2 casas decimais
        contas.append(conta(id=i, saldo_inicial=saldo_inicial))
    return contas

num_contas = 2  # Número de contas a serem criadas
contas = criar_contas(num_contas)

for conta in contas:
    print(f"Conta ID: {conta.getID()}, Saldo Inicial: {conta.getSaldo()}")

transacao = transferencia()

# Função para realizar a transferência em uma thread
def realizar_transferencia():
    transacao.transferir(contas[0], contas[1], 1000)

# Criar threads para realizar a transferência
thread1 = threading.Thread(target=realizar_transferencia)
thread2 = threading.Thread(target=realizar_transferencia)

# Iniciar as threads
thread1.start()
thread2.start()

# Aguardar as threads terminarem
thread1.join()
thread2.join()

