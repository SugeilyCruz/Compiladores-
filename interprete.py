#var nombre tipo; integer, string, real
from numpy import integer

class Variable:
    nombre = ""
    tipo = ""
    valor= ""
    def __init__(self, n, t, v):
        self.nombre = n
        self.tipo = t
        self.valor = v
        
def estaEnTabla(nombreVar):
    esta = False
    for v in tablaVar:
        if(v.nombre == nombreVar):
            esta = True
    return esta
# def estaEnTabla(nombreVar):
#     yaEsta = False
#     for v in tablaVar:
#         if (tablaVar[v].nombre==nombreVar):
#             yaEsta = True
#     return yaEsta

def agregaVar(ren):
    tipos=["integer","real","int","float","string","char"]
    datos = ren.split()
    nombreVar = datos[1]
    tipoVar = datos[2][:-1]
    if tipoVar in tipos:#El tipo de dato si esta en la lista
        if estaEnTabla(nombreVar):
            print(f"Variable redeclarada! {nombreVar}")
        else:
            tablaVar.append(Variable(nombreVar, tipoVar, ""))
    else:
        print("Tipo de dato enexistente:", tipoVar)
    pass
    
def muestraVar():
    print("variable \t tipo \t valor")
    for v in tablaVar:
        print(v.nombre,"\t",v.tipo,"\t",v.valor)
    pass

def esSeparador(caracter): #Funcion que trabaja en la Funcion tokeniza.
    return caracter in " \n\t"

def esSimboloEsp(caracter): #Funcion que trabaja en la Funcion tokeniza.
    return caracter in "+-*;,.:!=%&/()[]{}<><=>=:="

def esId(cad):
    return (cad[0] in "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

def tokeniza(cad):
    tokens = []
    dentro = False
    token = ""
    for c in cad:
        if dentro: #esta dentro del token
            if esSeparador(c): 
                tokens.append(token)
                token = ""
                dentro = False
            elif esSimboloEsp(c):
                tokens.append(token)
                tokens.append(c)
                token = ""
                dentro = False
            else:
                token = token + c
        else: #esta fuera del token
            if esSimboloEsp(c):
                tokens.append(c)
            elif esSeparador(c):
                a=0
            else:
                dentro = True
                token = c
    if token != '':
       tokens.append(token)
    return tokens

def setValor(variable, valor):
    encontrado= False
    for v in tablaVar:
        if (v.nombre == variable):
            encontrado= True
            v.valor=valor
    if not(encontrado):
        print("esa variable no existe")
    pass

def obtenerPrioridadOperador(o): # Función que trabaja con convertirInfijaA**.
    return {'(':1, ')':2, '+': 3, '-': 3, '*': 4, '/':4, '^':5}.get(o)

def obtenerListaInfija(cadena_infija):
    if(type(cadena_infija) == list):
        return obtenerListaInfija("".join(cadena_infija))
    '''Devuelve una cadena en notación infija dividida por sus elementos.'''
    infija = []
    cad = ''
    for i in cadena_infija:
       if i in['+', '-', '*', '/', '(', ')', '^', '=']:
           if cad != '':
               infija.append(cad)
               cad = ''
           infija.append(i)
       elif i == chr(32): # Si es un espacio.
           cad = cad
       else:
           cad += i
    if cad != '':
       infija.append(cad)
    return infija

def infija2Posfija(expresion_infija):
    '''Convierte una expresión infija a una posfija, devolviendo una lista.'''
    infija = obtenerListaInfija(expresion_infija)
    pila = []
    salida = []
    for e in infija:
        if e == '(':
            pila.append(e)
        elif e == ')':
            while pila[len(pila) - 1 ] != '(':
                salida.append(pila.pop())
            pila.pop()
        elif e in ['+', '-', '*', '/', '^']:
            while (len(pila) != 0) and (obtenerPrioridadOperador(e)) <= obtenerPrioridadOperador(pila[len(pila) - 1]):
                salida.append(pila.pop())
            pila.append(e)
        else:
            salida.append(e)
    while len(pila) != 0:
        salida.append(pila.pop())
    return salida


tablaVar = []

ren = ""
while (ren != "end;"):
    ren = input("ñ:")
    datos = tokeniza(ren)
    muestraVar()
    if(datos[0] == "var"):#primer elemento es var
        agregaVar(ren)
    elif esId(datos[0]):
        if (datos[1]=="="):#significa que es una asignacion a = (valor simple(5)-4tokens/expresion(5*2)-mas de 4tokens)
            if len(datos)==4:
                setValor(datos[0],datos[2])
            else: #asignaicon de expreseion
                d= ren.split("=") #separa en el =
                expresion=d[1][:-1]
                # print(expresion)
                posfija = infija2Posfija(expresion)
                print(posfija)
        elif (datos[0]=="print"): #si no es una asigancion
            # print(datos)
            if ('"' in datos[2]):
                print(datos[2])
            elif (datos[2] in tablaVar):
                print(datos[2])

