import datetime

def logWriteIn(conta: str, valor: float):
    try:
        arquivoLog = open("log.txt", "x")
    except:
        arquivoLog = open("log.txt", "a")
    
    arquivoLog.write(f"[{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] R${valor} depositados na conta {conta}\n")
    arquivoLog.close()

def logWriteOut(conta: str, valor: float):
    try:
        arquivoLog = open("log.txt", "x")
    except:
        arquivoLog = open("log.txt", "a")
    
    arquivoLog.write(f"[{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] R${valor} sacados da conta {conta}\n")
    arquivoLog.close()