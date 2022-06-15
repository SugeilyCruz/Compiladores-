class Pila: #Se crea la clase Pila(nos ayuda a generar la parte del codigo intermedio)
    arreglo = []
    def meter(self, dato):#Agrega datos a la Pila
        self.arreglo.append(dato)
    def sacar(self):#Saca datos de la Pila
        if (len(self.arreglo)==0):
            print("Pila vacia")
        else:
            return self.arreglo.pop()

def esOperador(v): #Funcion que trabaja con la parte del codigo intermedio
    return (v in "*/+-")

def esSeparador(caracter): #Funcion que trabaja en la Funcion tokeniza.
    return caracter in " \n\t"

def esSimboloEsp(caracter): #Funcion que trabaja en la Funcion tokeniza.
    return caracter in "+-*;,.:!=%&/()[]{}<><=>=:="

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


# prog = "a*b*c+d+e+f*g*a"
# tokens = tokeniza(prog)
# posfija = infija2Posfija(tokens)

posfija= "ab*c-de*-f-"
ct = 1
pila1 = Pila()
intermedio = []
codigo = []
for e in posfija:    
    if esOperador(e):
        op2 = pila1.sacar() #saca el ultimo valor dentro de nuestra pila, recordando que su estructura es LIFO.
        op1 = pila1.sacar() # Para ir en orden lo colocamos dentro de op2 y despues en op1
        cad = "t"+str(ct)+"="+op1+e+op2+";" # crea el codigo intermedio. op1 y op2 seran operandos mientras que e el operador
        intermedio.append(cad) #Cada codigo intermedio se va agregando a una lista "intermedio". 
        #Comenzamos a generar el codigo ensamblador, dependiendo de e a que operador es igual.
        print("LDA "+op1+";")#CARGA
        if e=="+":
            print("ADD "+op2+";")#SUMA
        elif e=="-":
            print("SUB "+op2+";")#RESTA
        elif e=="*":
            print("MUL "+op2+";")#MULTIPLICA
        elif e=="/":
            print("DIV "+op2+";")#DIVIDE
        pila1.meter("t"+str(ct)) # agregamos dentro de pila1 el orden de t dependiendo el contador.
        print("STA "+ "t"+str(ct)+";")#TOMA
        ct = ct + 1
    else:
        pila1.meter(e) #agregamos los operandos.
    
