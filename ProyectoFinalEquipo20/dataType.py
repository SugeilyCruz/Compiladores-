# - - - - - - - - - - -  - 
#metodos auxiliares

digitos = "0123456789"
punto = "."

def numeroEntero(cad):        #Esta función se encarga de determinar si un valor es un entero
    todoNum = True
    for c in cad:
        if not(c in digitos):
            todoNum = False
    return todoNum

def numeroFlotante(cad):      #Esta función se encarga de determinar si un valor es un flotante 
    p = 0
    numFlot = True
    if(cad[0] in digitos and cad[-1] in digitos): 
        for c in cad:
            if not(c in digitos):
                if(c in punto):
                    p = p + 1
                else:
                    numFlot = False
        if not(p == 1):
            numFlot = False  
    else:
        numFlot = False
    return numFlot

# - - - - - - - - - - -  -