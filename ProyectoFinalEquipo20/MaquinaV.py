from dataType import numeroEntero, numeroFlotante
import math

inst = []
param = []
pc = 0
ac = 0
memDatos = {}

archivo = open("programa.txt", "r") 
# archivo = open("trigonometricas.txt", "r")
# archivo = open("cadenas.txt", "r")
# archivo = open("programa.txt", "r")


for renglon in archivo:              
    datos = renglon.split()           

    if (len(datos)>0):               #Sí el tamaño del renglón es mayor a 0, ALMACENA una instrucción  

        inst.append(datos[0])        #Guarda los datos y los almacena en un arreglo, dependiendo la posición 
        param.append(datos[1][:-1])  #No almacena el  ;  ALMACENA los datos en la posición 1 hasta ANTESD del ;
archivo.close()                      #Se cierra el programa 


while (inst[pc]!="END"):                  #El ciclo sigue hasta que "PC" llegue a END 
    print ("{:^5}{:^5}{:^5}{:^8}{:^5}{:^5}{:^10}{:^5}".format("PC: ", pc, "  AC: ",ac," inst: ", inst[pc], "  parametro: ", param[pc])) 
    if (inst[pc]=="LDV"):                 #Si la instrucción en la posión de PC es LDV 
                                          #almacena el valor del parametro en el ACUMULADOR 
        ac = int(param[pc])
        pc = pc + 1                       #Incrementa el PC en +1

    elif (inst[pc]=="STA"):               #Si la instrucción en la posión de PC es STA
                                          #se almacena el valor en la posición actual 
        memDatos[param[pc]] = ac
        pc = pc + 1                       #Incrementa el PC en +1


    elif (inst[pc]=="LDA"):               #Si la instrucción en la posión de PC es LDA
        ac = memDatos[param[pc]]          #el valor que anteriormene se almacena en memDatos
        pc = pc + 1                       #Incrementa el PC en +1

    elif (inst[pc]=="ADD"):               #Si la instrucción en la posión de PC es ADD
                                          #se sumara a lo que este en el acumulador, se incrementa el valor de PC en +1
        ac = ac + memDatos[param[pc]]       
        pc = pc + 1

    elif (inst[pc]=="SUB"):               #Si la instrucción en la posión de PC es SUB, se resta lo que hay en el acumulador 
        x = ac - memDatos[param[pc]]     #posteriormente se almacena lo que este en la posición de PC      
        ac = float("{:.2f}".format(x))
        pc = pc + 1


    elif (inst[pc]=="MUL"):               #Si la instrucción en la posión de PC es MUL, se multiplica lo que hay en el acumulador , incrementa PC +1 y se almacena 
        x = ac * memDatos[param[pc]]
        ac = float("{:.2f}".format(x))
        pc = pc + 1 

    elif (inst[pc]=="DIV"):               #Si la instrucción en la posión de PC es DIV, se divide lo que hay en el acumulador y lo almacena en AC e incrementa +1
        ac = ac / memDatos[param[pc]]
        pc = pc + 1

    elif (inst[pc]=="JZ"):                #Se hace un SALTO CONDICIONAL 
                                          #si el valor de la línea es 0, el valor de PC es igual al valor que marque el acumulador 
        if (ac==0):               
            pc = int(param[pc])
        else:
            pc = pc + 1  

    elif (inst[pc]=="JMP"):              #Se hace un SALTO INCONDICIONAL, brinca a la línea que tenga el valor o parametro que le indiques. 
        pc = int(param[pc])              #Si la instrucción de PC es INC,tomara el valor que estaba en 
                                         #el acumulador, incrementa en +1 y lo almacena nuevamente 


    elif (inst[pc]=="INC"):              #Si la instrucción es INC, incrementa en +1
        valor = memDatos[param[pc]]        
        valor = valor + 1                # El valor toma el mismo valor que el parametro,
        memDatos[param[pc]] = valor      #en la posición de PC incrementa en +1 y lo guarda en la misma posición   
        pc = pc + 1       
    

    elif (inst[pc]=="SIN"):               #Si la instrucción es SIN, realiza la operación "seno" y la guarda en el acumulador

        x = float(math.sin((param[pc])))
        ac = float("{:.2f}".format(x))
        pc = pc + 1 

    elif (inst[pc]=="COS"):               #Si la instrucción es COS, realiza la operación "coseno" y la guarda en el acumulador

        x = float(math.cos((param[pc])))
        ac = float("{:.2f}".format(x))
        pc = pc + 1 

    elif (inst[pc]=="TAN"):               #Si la instrucción es TAN, realiza la operación "tangente" y la guarda en el acumulador

        x = float(math.tan((param[pc])))
        ac = float("{:.2f}".format(x))
        pc = pc + 1 
    
    elif (inst[pc]=="IN1"):     #INTERRUPCIONES
        print("Dame un valor entero: ")
        eteclado=input("€:")
        valor=eteclado[:-1]
        if(eteclado[-1]==";"):
            if(numeroEntero(valor)):    
                memDatos[param[pc]]=valor
                pc = pc + 1
            else:
                print("el dato ingresado no es tipo entero")
        else:
            print("se esperaba un ;")
        

    elif (inst[pc]=="IN2"):
        print("Dame un valor float: ")
        eteclado=input("€:")
        valor=eteclado[:-1]
        if(eteclado[-1]==";"):
            if(numeroFlotante(valor)):    
                memDatos[param[pc]]=valor
                pc = pc + 1
            else:
                print("el dato ingresado no es tipo flotante")
        else:
            print("se esperaba un ;")
        

    elif (inst[pc]=="IN3"):
        print("ingresa caracter")
        eteclado=input("€:")
        valor=eteclado[:-1]
        if(eteclado[-1]==";"):
            if(len(valor)==1):    
                memDatos[param[pc]]=valor
                pc = pc + 1
            else:
                print("el dato ingresado no es tipo char")
        else:
            print("se esperaba un ;")

    elif (inst[pc]=="IN4"):
        print("ingresa la cadena: ")
        memDatos[param[pc]]=str(input(""))
        pc = pc + 1

    elif (inst[pc]=="IN5"):     #IMPRIME ENTERO
        
        if(numeroEntero(memDatos[param[pc]])):
            print(memDatos[param[pc]])
        else:
            print("esta instruccion no corresponde al tipo de dato")
        pc = pc + 1


    elif (inst[pc]=="IN6"):     #IMPRIME FLOTANTE
        if(numeroFlotante(memDatos[param[pc]])):
            print(memDatos[param[pc]])
        else:
            print("esta instruccion no corresponde al tipo de dato")
        pc = pc + 1
        
    elif (inst[pc]=="IN7"):     #IMPRIME CHAR
        if(len(memDatos[param[pc]])==1):
            print(memDatos[param[pc]])
        else:
            print("esta instruccion no corresponde al tipo de dato")
        pc = pc + 1
        
    elif (inst[pc]=="IN8"):     #IMPRIME STRING
        print(memDatos[param[pc]])
        pc = pc + 1

    elif (inst[pc]=="IN9"):     #IMPRIME LO QUE HAYA ENEL CODIGO ENSAMBLADOR
        print(param[pc])
        pc = pc + 1
    

