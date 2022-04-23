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
    encuentraF = cad.find(".") 
    encuentraE = cad.find("e")
    if (encuentraF == -1) or (encuentraE >= 0): 
        return False
    else:
        return True
    
def exponencial(cad):#E ante y al final, . menor a e y - despues de e o en la posicion 0.
    cad = str.lower(cad) 
    encuentraE = cad.find("e")
    encuentraF = cad.find(".") 
    encuentraM = cad.find("-")
    if (encuentraE == -1) or (encuentraE==0) or (encuentraE==len(cad)-1)\
    or (encuentraF > encuentraE) or ((encuentraM != encuentraE+1) and (encuentraM != -1) and (encuentraM !=0)): 
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
        return("Error")

#Casos de Prueba
token1="12312" #Entero
print(numero(token1))
token2="123.12" #Float
print(numero(token2))
token10="-123.12" #Float
print(numero(token10))
token6="12.312e12" #Exponencial
print(numero(token6))
token7="-12.312e12" #Exponencial
print(numero(token7))
token8="12.312e-12" #Exponencial
print(numero(token8))
#Casos de Prueba Error
token9="12.31-2e12"
print(numero(token9))
token3="e123.12" 
print(numero(token3))
token4="12e.312" 
print(numero(token4))
token5="12.312e" 
print(numero(token5))