#var nombre tipo; integer, string, real
from turtle import pos


class Variable:
    nombre = ""
    tipo = ""
    valor= ""
    def __init__(self, n, t, v):
        self.nombre = n
        self.tipo = t
        self.valor = v

tablaVar = []

def esSeparador(caracter):
    return caracter in " \n\t"

def esSimboloEsp(caracter):
    return caracter in "+-*;,.:!=%&/()[]{}<><=>=:="

def tokeniza(cad):
    tokens = [] #Nuestra lista vacia
    dentro = False #Esta variable nos va indicar si el caracter esta dentro o fuera del token
    token = ""
    for c in cad: 
        if dentro:
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
        else:
            if esSimboloEsp(c):
                tokens.append(c)
            else:
                dentro = True
                token = c

    tokens.append(token)
        
    return tokens

def obtenerPrioridadOperador(o):
    #Función que trabaja con convertirInfijaA**.
    return {'(':1, ')':2, '+': 3, '-': 3, '*': 4, '/':4, '^':5}.get(o)

def obtenerListaInfija(cadena_infija):
    if(type(cadena_infija) == list):
        return obtenerListaInfija("".join(cadena_infija))#Une la lista en una cadena si el parametro es una lista
    '''Devuelve una cadena en notación infija dividida por sus elementos, devuelve una lista.'''
    infija = []
    cad = ''
    for i in cadena_infija:
        #Se verifica si el caracter es un operador
       if i in['+', '-', '*', '/', '(', ')', '^', '=']:
           #Se verifica si la cadena no esta vacía
           if cad != '':
               infija.append(cad) #Se añade
               cad = '' #Se asigna un vacio a cad
           infija.append(i)
       elif i == chr(32): #Se verifica si es un espacio.
           cad = cad #No se hace ningún cambio en cad
       else:
           cad += i #Se concatena el caracter de i a la cadena
    #Si la cadena no está vacía, se añade a la lista "infija" 
    if cad != '':
       infija.append(cad)
    return infija

def infija2Posfija(expresion_infija):
    '''Convierte una expresión infija a una posfija, devolviendo una lista.
       Utilizamos el método de pila visto en clase, aplicado en un programa.'''
    infija = obtenerListaInfija(expresion_infija) #Asignamos la expresión infija a la variable infija 
    pila = []
    salida = []

    for e in infija:
        if e == '(': #Si encuentra un '(' lo agrega directamente a la pila 
            pila.append(e)
        elif e == ')':
            while pila[len(pila) - 1 ] != '(': #Este while agrega todo lo que haya entre los parentesis
                salida.append(pila.pop())
            pila.pop() #Se quita el último elemento de la pila
        elif e in ['+', '-', '*', '/', '^']: #Se verifica si el elemento es un operador
            #Mientras la pila no esté vacía y la prioridad del elemento evaluado sea menor o igual a la del
            #último elemento de la pila
            while (len(pila) != 0) and (obtenerPrioridadOperador(e)) <= obtenerPrioridadOperador(pila[len(pila) - 1]):
            #Se usa la función "obtenerPrioridadOperador()" ya que tiene organizados los operadores
            #por jerarquía de operaciones
                salida.append(pila.pop()) #Se añade el último elemento de la pila a la salida
            pila.append(e) #Se agrega el elemento evaluado a la pila
        else: #Si no es un operador se agrega a la salida
            salida.append(e)

    while len(pila) != 0: #Mientras la pila no esté vacía
        salida.append(pila.pop()) #Se añade el último elemento de la pila a la salida
    return salida

def esId(cad):
    return (cad[0] in "_abcdefghijklnmopqrstuvwxyzABCEFGHIJKLMNOPQRSTUVWXYZ")

def estaEnTabla(nombreVar):
    esta = False
    for v in tablaVar:
        if(v.nombre == nombreVar):
            esta = True
    return esta

def agregaVar(renglon):
    tipos = ["integer", "real", "boolean", "string"]
    datos = renglon.split()
    nombreVar = datos[1]
    tipoVar = datos[2][:-1]
    if(tipoVar in tipos):   
        if(estaEnTabla(nombreVar)):
            print("Variable redeclarada", nombreVar)
        else:
            tablaVar.append(Variable(nombreVar, tipoVar, ""))
    else:
        print("tipo de dato inexistente", tipoVar)
    
def muestraVar():
    print("Variable \t tipo \t valor")
    for v in tablaVar:
        print(v.nombre, " \t", v.tipo, " \t", v.valor)

def setValor(variable, valor):
    encontrado = False
    for v in tablaVar:
            if(v.nombre == variable):
                encontrado = True
                v.valor = valor
    if not(encontrado):
        print("Esa variable no existe")

def getValor(variable):
    pass



ren = ""
while (ren != "end;"):
    ren = input("@:")
    datos = tokeniza(ren)[0:-1]
    if(datos[0] == "var"):
        agregaVar(ren)
    elif (esId(datos[0])):
        if(datos[1] == "="): #es una asigancion            
            if(len(datos) == 4):
                setValor(datos[0], datos[2])
            else: #Asignacion de una expresion
                d = ren.split("=")
                expresion = d[1][:-1]
                posfija = infija2Posfija(expresion)
                print(posfija)

muestraVar()
        