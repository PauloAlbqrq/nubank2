# 2º ADS
# Paulo Ximenes
# Eduarda Leigue
# Matheus Henrique
# Luiz Guilherme
# João do Monte

import datetime, time, threading, random

# Classe que representa uma conta bancária
class conta:
    def __init__(self, id, saldoInicial):
        self.id = id
        self.saldo = saldoInicial
        self.lock = threading.Lock()  # Lock para garantir a consistência das transferências

# Classe que representa uma transferência bancária
class transferencia:
    def __init__(self):
        self.log = []
        self.transaction_id = 0

    # Função para adicionar mensagens ao log
    def logFun(self, mensagem):
        self.log.append(f"[{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] {mensagem}")

    # Função para escrever o log em um arquivo
    def logWrite(self):
        try:
            with open('log.txt', 'x') as f:
                for line in self.log:
                    f.write(line)
        except FileExistsError:
            with open('log.txt', 'a') as f:
                for line in self.log:
                    f.write(line)
    
    # Função para realizar a transferência entre duas contas
    def transferir(self, contaOrigem, contaDestino, valor):
        if contaOrigem.saldo < valor:
            print("Transferência não realizada: saldo insuficiente")
            self.logFun("Transferência não realizada: saldo insuficiente\n")
        else:
            # Ordena as contas para evitar deadlock
            if contaOrigem.id > contaDestino.id:
                contaMaiorId = contaOrigem
                contaMenorId = contaDestino
            else:
                contaMaiorId = contaDestino
                contaMenorId = contaOrigem
            
            # Bloqueia as contas para realizar a transferência
            with contaMenorId.lock:
                with contaMaiorId.lock:
                    contaOrigem.saldo -= valor
                    contaDestino.saldo += valor
                    print(f"R${valor:.2f} transferido de {contaOrigem.id} para {contaDestino.id} | Saldo final de {contaOrigem.id}: R${contaOrigem.saldo:.2f} | Saldo final de {contaDestino.id}: R${contaDestino.saldo:.2f}")
                    self.logFun(f"R${valor:.2f} transferido de {contaOrigem.id} para {contaDestino.id} | Saldo final de {contaOrigem.id}: R${contaOrigem.saldo:.2f} | Saldo final de {contaDestino.id}: R${contaDestino.saldo:.2f}\n")

# Cenário simples de transferência entre duas contas
def cenarioSimples():
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
    transacao.logWrite()

# Cenário de alta concorrência com múltiplas contas e transferências
def altaConcorrencia():
    saldoTotalInicial = 0
    num_contas = 100  # Número de contas a serem criadas
    contas = []
    for i in range(num_contas):
        saldo_inicial = round(random.uniform(1000, 5000), 2)  # Saldo inicial aleatório entre 1000 e 5000 com 2 casas decimais
        contas.append(conta(id=i, saldoInicial=saldo_inicial))

    for c in contas:
        print(f"Conta ID: {c.id}, Saldo Inicial: {c.saldo}")
        saldoTotalInicial += c.saldo

    print(f"\033[93mSaldo total inicial: {saldoTotalInicial:.2f}\033[0m")

    # Função para realizar transferências aleatórias entre contas
    def realizar_transferencias(contas, transacao):
        for _ in range(100):
            conta_origem = random.choice(contas)
            conta_destino = random.choice(contas)
            while conta_origem == conta_destino:
                conta_destino = random.choice(contas)
            valor = random.randint(100, 5000)
            transacao.transferir(conta_origem, conta_destino, valor)

    transacao = transferencia()
    listaThreads = []
    for obj in range(50):
        listaThreads.append(threading.Thread(target=realizar_transferencias, args=(contas, transacao)))
        listaThreads[obj].start()

    for t in listaThreads:
        t.join()

    saldoTotalFinal = 0
    for c in contas:
        saldoTotalFinal += c.saldo
    print(f"\033[93mSaldo total final: {saldoTotalFinal:.2f}\033[0m")
    transacao.logWrite()
    print(len(transacao.log))

# Cenário de transferência com saldo insuficiente
def saldoInsuficiente():
    ct1 = conta(1, 100)
    ct2 = conta(2, 200)
    ct3 = conta(3, 300)
    ct4 = conta(4, 400)
    ct5 = conta(5, 500)

    transacao = transferencia()

    T1 = threading.Thread(target=transacao.transferir, args=(ct1, ct2, 600))
    T2 = threading.Thread(target=transacao.transferir, args=(ct2, ct3, 1000))

    T1.start()
    T2.start()

    T1.join()
    T2.join()
    transacao.logWrite()

# Executa os cenários
cenarioSimples()
altaConcorrencia()
saldoInsuficiente()