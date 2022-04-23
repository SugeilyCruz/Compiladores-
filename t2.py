def entero(cad):
    cad = str(cad)
    digitos = "0123456789"
    todosNum = True
    for c in cad: 
        if not (c in digitos):
            todosNum = False 
    return todosNum 

def flotante(cad):
    cad = str.lower(cad)
    if (cad.find(".")  == -1) or (cad.find("e") >= 0): 
        return False
    else:
        return True
    
def exponencial(cad):
    cad = str.lower(cad) 
    if (cad.find("e") == -1) or (cad.find("e") == len(cad)-1) or (cad.find("e")==0) or (cad.find(".")  > cad.find("e")): 
        return False
    else:
        return True
    
def numero(cad):
    if entero(cad):
        return("Entero")
    elif flotante(cad):
        return("Float")
    elif exponencial(cad):
        return("Exponencial")
    else:
        return("Numero erroneo")

token1="46" 
print(numero(token1))
token2="78.2" 
print(numero(token2))
token3="-87.23" 
print(numero(token3))
token4="45.8e12" 
print(numero(token4))
token5="12.12e233" 
print(numero(token5))
token6="343e.34" 
print(numero(token6))
token7="902" 
print(numero(token7))
