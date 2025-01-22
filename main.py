import random
import threading
from conta import conta
from transferencia import transferencia
import time



def transferenciaSimples():
    ct1 = conta(1, 100)
    ct2 = conta(2, 200)
    ct3 = conta(3, 300)
    ct4 = conta(4, 400)
    ct5 = conta(5, 500)

    transacao = transferencia()

    T1 = threading.Thread(target=transacao.transferir, args=(ct1, ct2, 50))
    T2 = threading.Thread(target=transacao.transferir, args=(ct2, ct3, 50))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

def altaConcorrencia():
    saldoTotalInicial = 0
    num_contas = 100  # Número de contas a serem criadas
    contas = []
    for i in range(num_contas):
        saldo_inicial = round(random.uniform(1000, 5000), 2)  # Saldo inicial aleatório entre 1000 e 5000 com 2 casas decimais
        contas.append(conta(id=i, saldo_inicial=saldo_inicial))

    for c in contas:
        print(f"Conta ID: {c.getID()}, Saldo Inicial: {c.getSaldo()}")
        saldoTotalInicial += c.getSaldo()

    print(f"\033[93mSaldo total inicial: {saldoTotalInicial:.2f}\033[0m")

    def realizar_transferencias(contas, transacao):
        for _ in range(1):
            conta_origem = random.choice(contas)
            conta_destino = random.choice(contas)
            valor = random.randint(100, 5000)
            transacao.transferir(conta_origem, conta_destino, valor)
            time.sleep(random.uniform(0.1, 0.5))  # Simula uma pequena latência entre as operações

    transacao = transferencia()
    listaThreads = []
    for obj in range(500):
        listaThreads.append(threading.Thread(target=realizar_transferencias, args=(contas, transacao)))
        listaThreads[obj].start()


    
    for t in listaThreads:
        t.join()

    saldoTotalFinal = 0
    for c in contas:
        saldoTotalFinal += c.getSaldo()
    print(f"\033[93mSaldo total final: {saldoTotalFinal:.2f}\033[0m")

# transacao = transferencia()

# # Função para realizar a transferência em uma thread
# def realizar_transferencia():
#     transacao.transferir(contas[0], contas[1], 1000)

# # Criar threads para realizar a transferência
# thread1 = threading.Thread(target=realizar_transferencia)
# thread2 = threading.Thread(target=realizar_transferencia)

# # Iniciar as threads
# thread1.start()
# thread2.start()

# # Aguardar as threads terminarem
# thread1.join()
# thread2.join()

#transferenciaSimples()
altaConcorrencia()