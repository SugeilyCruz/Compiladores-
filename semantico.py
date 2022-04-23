class Variable:
    nombre = ""
    tipo = ""
    valor = ""
    def __init__(self, n, t, v):
        self.nombre = n
        self.tipo = t
        self.valor = v
    
def esSeparador(c):
    separadores = "\n\t "
    return c in separadores

def esSimboloEsp(c):
    especiales = "¡#$%&/*+-=:;[]{}(),"
    return c in especiales

def quitaComentarios(cad):
    # estados: A, B, C, Z
    estado ="Z"    
    #cad = "a=b/c;"
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

def tokeniza(cad):
    tokens = []
    dentro = False
    token = ""
    for c in cad:
        if dentro:  #esta dentro del token
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
    return tokens

def esId(cad):
    return (cad[0] in "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

def esPalReservada(cad):
    reservadas = ["main","char", "int","float","double","if","else","do","while","for","switch","short","long","extern", "static","default","continue","break","register","sizeof","typedef"]
    return cad in reservadas

def esTipo(cad):
    tipos=["integer", "char", "real", "string"]
    return cad in tipos

programa ="var\n\tvar1, var2 : real;\n\tvar3, nom : string;\n"\
           "begin\n\tvar2 = (var1*var3)/var2;"
tokens = tokeniza(programa)
#print(programa)
estado = "z"
variables=[]
for token in tokens:
    if (estado=="z"):
        if (token=="var"):
            estado="a"        
    elif (estado=="a"):
        if esId(token):
            estado = "b"            
            repetido = False
            for v in variables:
                if (v.nombre==token):
                    repetido = True
            if (repetido):
                print("variable redeclarada!!")
                print(token)
                estado = "z"
            else:
                variables.append(Variable(token, "", ""))
                                   
    elif (estado == "b"):
        if (token==":"):
            estado = "c"
            #print("token:", token, "estado:", estado)
        elif (token==","):
            estado ="a"
    elif (estado == "c"):
        if esTipo(token):
            estado = "d"
            #print("token:", token, "estado:", estado)            
            for v in variables:
                if (v.tipo == ""):
                    v.tipo = token
    elif (estado=="d"):
        if (token==";"):
            estado = "e"
            #print("token:", token, "estado:", estado)
    elif (estado == "e"):
        if (token=="begin"):
            estado = "z"
            #print("token:", token, "estado:", estado)
            #print ("todo bien")
        elif esId(token):
            estado = "a"
            repetido = False
            for v in variables:
                if (v.nombre==token):
                    repetido = True
            if (repetido):
                print("variable redeclarada!!")
                print(token)
                estado = "z"
            else:
                variables.append(Variable(token, "", ""))

for v in variables:
    print(v.nombre, v.tipo)
        
        
