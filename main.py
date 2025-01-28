import datetime, time, threading, random

class conta:
    def __init__(self, id, saldoInicial):
        self.id = id
        self.saldo = saldoInicial
        self.lock = threading.Lock()
    
class transferencia:
    def __init__(self):
        self.log = []
        self.transaction_id = 0

    def logFun(self, mensagem):
        self.log.append(f"[{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] {mensagem}")

    def logWrite(self):
        try:
            with open('log.txt', 'x') as f:
                for line in self.log:
                    f.write(line)
        except FileExistsError:
            with open('log.txt', 'a') as f:
                for line in self.log:
                    f.write(line)
    
    def transferir(self, contaOrigem, contaDestino, valor):
        if contaOrigem.saldo < valor:
            print("Transferência não realizada: saldo insuficiente")
            self.logFun("Transferência não realizada: saldo insuficiente\n")
        else:
            if contaOrigem.id > contaDestino.id:
                contaMaiorId = contaOrigem
                contaMenorId = contaDestino
            else:
                contaMaiorId = contaDestino
                contaMenorId = contaOrigem
            
            with contaMenorId.lock:
                with contaMaiorId.lock:
                    contaOrigem.saldo -= valor
                    contaDestino.saldo += valor
                    print(f"R${valor:.2f} transferido de {contaOrigem.id} para {contaDestino.id} | Saldo final de {contaOrigem.id}: R${contaOrigem.saldo:.2f} | Saldo final de {contaDestino.id}: R${contaDestino.saldo:.2f}")
                    self.logFun(f"R${valor:.2f} transferido de {contaOrigem.id} para {contaDestino.id} | Saldo final de {contaOrigem.id}: R${contaOrigem.saldo:.2f} | Saldo final de {contaDestino.id}: R${contaDestino.saldo:.2f}\n")

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

cenarioSimples()
altaConcorrencia()
saldoInsuficiente()