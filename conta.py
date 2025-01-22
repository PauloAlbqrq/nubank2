import threading

class conta:
    def __init__(self, id, saldo_inicial):
        self.__id = id
        self.__saldo = saldo_inicial
        self.lock = threading.Semaphore(1)
        
    def getID(self):
        return self.__id
    
    def getSaldo(self):
        return self.__saldo
    
    # concede o semáforo a uma thread
    # def acquireSemaphore(self):
    #     return self.__semaphore.acquire(blocking=False)
    
    # devolve o semáforo para a conta depois da thread realizar a transferência
    # def releaseSemaphore(self):
    #     if self.__semaphore._value == 0:
    #         self.__semaphore.release()
            
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            return True
        else:
            print("Valor inválido")
            return False
            
    def sacar(self, valor):
        if valor > 0 and valor<=self.__saldo:
            self.__saldo -= valor
            return True
        else:
            print("operação inválida")
            return False
