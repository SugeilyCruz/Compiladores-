# Realice un compilador de una versión recortada de lenguaje “C”, el cual cuente con las siguientes 
# características:
from numpy import integer

#Sólo se declara una variable por línea de la forma
class Variable: 
    nombre = ""
    tipo = ""
    valor= ""
    direccion= 0
    def __init__(self, n, t, v,d):
        self.nombre = n
        self.tipo = t
        self.valor = v
        self.direccion = d

# Al programa primero se le deben quitar los comentarios para que quede de la siguiente forma
def quitaComentarios(cad):
    estado ="Z"
    cad2 =""
    for c in cad:
        if (estado=="Z"):
            if (c=="/"):
                estado = "A"
            else:
                cad2 = cad2 + c
        elif (estado=="A"):
            if (c=="*"):
                estado="B"
            else:
                estado = "Z"
                cad2=cad2+"/"+c
        elif (estado=="B"):
            if (c=="*"):
                estado = "C"
        elif(estado=="C"):
            if (c=="/"):
                estado="Z"
            else:
                estado="B"
    return cad2

#Separa en tokens
def esSeparador(caracter): 
    return caracter in " \n\t"

def esSimboloEsp(caracter):
    return caracter in "+-*;,.:!=%&/()[]{}<><=>=:="

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

#Debe crear una tabla de variables donde vaya almacenando cada variable de la siguiente manera:
def estaEnTabla(nombreVar): 
    esta = False
    for v in tablaVar:
        if(v.nombre == nombreVar):
            esta = True
    return esta

def agregaVar(ren,c):
    tipos=["int","float","string","char"] #Tipos de datos
    datos = ren.split()
    nombreVar = datos[2][:-1]
    tipoVar = datos[1]
    if tipoVar in tipos:
        if estaEnTabla(nombreVar): #verificar que dicha variable no se encuentre en la tabla.
            print(f"Variable redeclarada! {nombreVar}")
        else:
            tablaVar.append(Variable(nombreVar, tipoVar, "",c))
    else:
        print("Tipo de dato enexistente:", tipoVar)
    pass

def muestraVar():
    print("nombre \t tipo \t valor \t direccion")
    cont=0
    for v in tablaVar:
        print(v.nombre,"\t",v.tipo,"\t",v.valor,"\t",v.direccion)
    pass

#Todos los “read” y “print” serán reemplazados por interrupciones
def cambiaPR(cat):
    cad=tokeniza(cat)
    cad2 =""
    for c in cad:
        if (c=="read"):
            for n in cad:
                if estaEnTabla(n):
                    for v in tablaVar:
                        if (v.nombre == n):
                            if v.tipo == "float":
                                c="IN2"
                            elif v.tipo == "int":
                                c="IN1"
                            elif v.tipo == "string":
                                c="IN4"
                            elif v.tipo == "char":
                                c="IN3"
        cad2 = cad2 + " " + c
    return cad2

# Las asignaciones que involucren expresiones tales como:
def esId(cad):
    return (cad[0] in "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

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

#PRUEBAAAAAAAAA
tablaVar = []
archivo = open("ansu.txt", "r")
c=0
for ren in archivo:
    datos = quitaComentarios(ren)#1
    if (datos != "end;"):
        datos1 = cambiaPR(datos)#3
        tok = tokeniza(datos1)
        if(tok[0] == "var"):#2
            agregaVar(datos,c)
            c+=1
        elif (tok[0]=="print"):
            print(ren[7:-4])
        elif (tok[0]=="IN2"):#3
            for n in tok:
                if estaEnTabla(n):
                    for v in tablaVar:
                        if v.nombre == n:
                            v.valor=input(f"{n} :")       
        elif (datos[1]=="="):#4
            if len(datos)==4:
                setValor(datos[0],datos[2])
            else:
                d= ren.split("=") 
                expresion=d[1][:-1]
                posfija = infija2Posfija(expresion)
                print(posfija)
        
archivo.close()
muestraVar()

#para asignar valor con la direccion
        # elif(tok[0] == "print"):#3
        #     for n in tok:
        #         if estaEnTabla(n):
        #             for v in tablaVar:
        #                 if v.nombre == n:
        #                     v.valor=input(f"{n} :")