import random
clientes=["luis","pablo","andres"]
datos=[125474454,444544,6688777]
fechadenacimiento=["15 de agosto 1989","8 de septiembre 1970","17 de septiembre1980"]

todojunto = clientes+datos+fechadenacimiento
nombre=input("ingrese un nombre para verificar si esta en el sistema :v")
if nombre=="luis" :
    print (datos[0],",",fechadenacimiento[0]) # 1
elif nombre=="pablo" :
    print (datos[1],",",fechadenacimiento[1])
elif nombre=="andres" :
    print (datos[2],",",fechadenacimiento[2])
else:
    print("no existe este usurio")
d=input("desea aumentar un nuevo cliente: ")  
if d=="si":
    nuevocliente=input()
    clientes.append(nuevocliente)
    print(clientes)
else:
    print("ok")
nom=input("seleccione el nombre de la lista que desea deshabilitar: ")
if nom=="luis":
    clientes.remove("luis")
    print("la lista de habilitados es" ,clientes,"pero luis esta deshabilitado")
elif nom=="pablo":
    clientes.remove("pablo")
    print("la lista de habilitados es ",clientes,"pero pablo esta deshabilitado")
elif nom=="andres":
    clientes.remove("andres")
    print("la lista de habilitados es ",clientes,"pero andres esta deshabilitado")
elif nom==nuevocliente:
    clientes.remove(nuevocliente)
    print("la lista de habilitados es ",clientes,"pero",nuevocliente,"esta deshabilitado")

else:
    print("no existe este usuario")
cnt1=10000
cnt2=20000
cnt3=100
cnt4=50000
e=(input("desea depositar o retirar dinero de su cuenta?: "))
if e=="depositar":
    n=input("ingrese el nombre del cliente: ")
    if n=="luis":
        can1=int(input("ingrese la cantidad de dinero que desea depositar: "))
        c1=cnt1+can1
        print("su saldo actual es: ",c1)
    elif n=="pablo":
        can2=int(input("ingrese la cantidad de dinero que desea depositar: "))
        c2=cnt2+can2
        print("su saldo actual es: ",c2)

    elif n=="andres":
        can3=int(input("ingrese la cantidad de dinero que desea depositar: "))
        c3=cnt3+can3
        print("su saldo actual es: ",c3)

    elif n==nuevocliente:
        can4=int(input("ingrese la cantidad de dinero que desea depositar: "))
        c4=cnt4+can4
        print("su saldo actual es: ",c4)
    else:
        print("no existe este usuario")
elif e=="retirar":
    n=input("ingrese el nombre del cliente: ")
    if n=="luis":
        can1=int(input("ingrese la cantidad de dinero que desea retirar: "))
        c1=cnt1-can1
        print("su saldo actual es: ",c1)
    elif n=="pablo":
        can2=int(input("ingrese la cantidad de dinero que desea retirar: "))
        c2=cnt2-can2
        print("su saldo actual es: ",c2)

    elif n=="andres":
        can3=int(input("ingrese la cantidad de dinero que desea retirar: "))
        c3=cnt3-can3
        print("su saldo actual es: ",c3)

    elif n==nuevocliente:
        can4=int(input("ingrese la cantidad de dinero que desea retirar: "))
        c4=cnt4-can4
        print("su saldo actual es: ",c4)        
    else:
        print("no existe este usuario")
else:
    print("no sea payaso :v")
y=0.5  
usuario=input("ingrese el nombre de usuario: ")
if usuario=="luis":
    milla=cnt1*y
    print("su milla es",milla)
elif usuario=="pablo":
    milla=cnt2*y
    print("su milla es",milla)
elif usuario=="andres":
    milla=cnt3*y
    print("su milla es",milla)
elif usuario==nuevocliente:
    milla=cnt4*y 
    print("su milla es",milla)
else:
    print("no existe")
t=100
g1=cnt1/t
g2=cnt2/t
g3=cnt3/t
g4=cnt4/t
if g1>g2 and g3 and g4:
    print("luis es tiene mas probabilidad de ganar 100.000BS")
elif g2>g1 and g3 and g4:
    print("pablo es tiene mas probabilidad de ganar 100.000BS")
elif g3>g1 and g2 and g4:
    print("andres es tiene mas probabilidad de ganar 100.000BS")
elif g4>g1 and g2 and g3:
    print(nuevocliente," es tiene mas probabilidad de ganar 100.000BS")   
else:
    print("nadie va ha ganar")
    
            
            
    
    
 
    
       