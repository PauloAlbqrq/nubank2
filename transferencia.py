import datetime
from conta import conta

class transferencia:
    def _init_(self):
        self.log = []

        self.transaction_id = 0

        print('Transações inicializando...')
    
    def logWrite(self, contaOrigem: conta, contaDestino: conta, valor: float):
        try:
            arquivoLog = open("log.txt", "x")
        except FileExistsError:
            arquivoLog = open("log.txt", "a")
        
        arquivoLog.write(f"[{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] R${valor} transferido de {contaOrigem.getID()} para {contaDestino.getID()} | Saldo final de {contaOrigem.getID()}: R${contaOrigem.getSaldo()} | Saldo final de {contaDestino.getID()}: R${contaDestino.getSaldo()}\n")
        arquivoLog.close()

    def transferir(self, conta_origem, conta_destino, valor):
        menor_id = 0
        if conta_origem.getID() < conta_destino.getID():
            menor_id = conta_origem
            maior_id = conta_destino
        else:
            menor_id = conta_destino
            maior_id = conta_origem
        
        with menor_id.lock:
            with maior_id.lock:
                if conta_origem.sacar(valor):
                    conta_destino.depositar(valor)
                    self.logWrite(conta_origem, conta_destino, valor)
                    print(f"Transferência concluída.\nSaldo final de {conta_origem.getID()}: R${conta_origem.getSaldo()}\nSaldo final de {conta_destino.getID()}: R${conta_destino.getSaldo()}")
                else:
                    print(f"Saldo insuficiente para transferência.\nSaldo atual de {conta_origem.getID()}: R${conta_origem.getSaldo()}")


