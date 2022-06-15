def esOperador(c):
    return c in "*/-+"

pila = []       
posfija = ["2","3","*","4","5","*","+"]
for e in posfija:
    if esOperador(e):   #es operador
        op2 = float(pila.pop())
        op1 = float(pila.pop())
        if (e == "*"):
            r = op1 * op2 #codigo intermedio
        elif (e == "+"):
            r = op1 + op2
        elif (e == "-"):
            r = op1 - op2
        elif (e == "/"):
            r = op1 / op2
        pila.append(r)
        #print(pila)
    else:               #es operando
        pila.append(e)
        # print(pila)
print(pila[0])