import os
import socket

def obtenAccesoHF():
    if local_check():
        print("Estoy en LOCAL...")        
        import bridges
        llave = bridges.llave
    else:
        print("Estoy en REMOTO...")
        llave = os.getenv("llave")

        print("Ésto es llave:", llave)


    return llave

def local_check(): 

    hostname = socket.gethostname()
    #r-moibe-nowme
    print("Dentro de local_check... , el hostname es: ", hostname)

    if "r-moibe-nowme" in hostname:
        print("Ejecutando en el servidor")
        return False
    else:
        print("Ejecutando en local")
        return True