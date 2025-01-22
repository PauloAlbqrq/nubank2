class transferencia:
    def _init_(self):
        self.log = []

        self.lock = Lock() # os poggers vão resolver dps

        self.transaction_id = 0

        print('Transações inicializando...')

    def transferir(conta_origem, conta_destino, valor):
        menor_id = 0
        if conta_origem.getID() < conta_destino.getID():
            menor_id = conta_origem.getID()
        else:
            menor_id = conta_destino.getID()
