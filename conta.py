class conta:
    def _init_(self, id, saldo_inicial):
        self.__id = id
        self.__saldo = saldo_inicial
        self.__lock = True
        
    def getID(self):
        return self.__id
    
    def getSaldo(self):
        return self.__saldo
    
    # concede o lock a uma thread
    def getLock(self):
        if self.__lock != False:
            return True
            self.__lock = False
    
    # devolve o lock para a conta depois da thread realizar a transferência
    def returnLock(self):
        if self.__lock == False:
            self.__lock
            
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Valor inválido")
            
    def sacar(self, valor):
        if valor > 0 and valor<=self.__saldo:
            self.__saldo -= valor
        else:
            print("operação inválida")
