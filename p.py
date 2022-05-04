a=13
b="Hola"
print(type(a))
if (type(a)=='int'):
    print("Hola")


tablaVar = []
archivo = open("ansu.txt", "r")
c=0
d=0
for ren in archivo:
    d+=1
    datos = quitaComentarios(ren)#1
    if (";" in datos):
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
            elif (tok[1]=="="):#4
                if len(datos)==4:
                    setValor(datos[0],datos[2])#probar
                else:
                    d= ren.split("=") 
                    expresion=d[1][:-2]
                    posfija = infija2Posfija(expresion)
                    print(posfija)        
    else:
        print(f"Error falta ; en la linea {d}")
        break
archivo.close()