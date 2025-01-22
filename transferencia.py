import datetime

class transferencia:
    def _init_(self):
        self.log = []

        self.transaction_id = 0

        print('Transações inicializando...')
    
    def logWrite(conta: str, valor: float):
        try:
            arquivoLog = open("log.txt", "x")
        except FileExistsError:
            arquivoLog = open("log.txt", "a")
        
        arquivoLog.write(f"[{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] R${valor} depositados na conta {conta}\n")
        arquivoLog.close()

    def transferir(conta_origem, conta_destino, valor):
        menor_id = 0
        if conta_origem.getID() < conta_destino.getID():
            menor_id = conta_origem.getID()
        else:
            menor_id = conta_destino.getID()
    

