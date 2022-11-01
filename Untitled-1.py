import math
def cal_ffe(a,b):
    ffe=a*b
    return ffe
def cal_ffd(a,b):
    ffd=a*b
    return ffd
m=float(input("Ingrese la masa del cuerpo en Kg"))
f=float(input("Ingrese la fuerza aplicada al cuerpo en -Newton- (Ingresar valor en negativo para mover el objeto hacia la direccion opuesta) "))
g=9.8
fx=f
pesoy=m*g
if input("¿El plano esta inclinado? (s/n) ").lower()=="s":
    grados=int(input("¿Cuantos grados(°) esta inclinado el plano? "))
    while grados>90 or grados<0:
        print("No es posible, ingrese otro valor ")
        grados=int(input("¿Cuantos grados(°) estaaa1 inclinado el plano? "))
    fx=fx+m*g*math.sin(grados*math.pi/180)
    pesoy=m*g*math.cos(grados*math.pi/180)
if input("¿Hay friccion? (s/n) ").lower()=="s":
    material=input("¿De que materiales son los objetos?\n1. Madera sobre madera\n2. Acero sobre hielo\n3. Teflón sobre teflón\n4. Caucho sobre cemento seco\n5. Vidrio sobre vidrio\n6. Esquí sobre nieve\n7. Madera sobre cuero\n8. Aluminio sobre acero\n9. Articulaciones humanas\n10. Otro\n")
    if material=="1":ue=0.5;ud=0.3
    elif material=="2":ue=0.03;ud=0.02
    elif material=="3":ue=0.04;ud=0.04
    elif material=="4":ue=1;ud=0.8
    elif material=="5":ue=0.9;ud=0.4
    elif material=="6":ue=0.1;ud=0.05
    elif material=="7":ue=0.5;ud=0.4
    elif material=="8":ue=0.61;ud=0.47
    elif material=="9":ue=0.02;ud=0.003
    elif material=="10":
        ue=float(input("Ingrese el coeficiente de friccion estatico: "))
        ud=float(input("Ingrese el coeficiente de friccion dinamico: "))
    ffe=cal_ffe(ue,pesoy)
    ffd=cal_ffd(ud,pesoy)
    fuerzaNeta=fx-ffd
    if ffe>abs(fx):
        print("Fuerza Aplicada:",f,"Newton\nFuerza de Friccion Estatica:",ffe,"Newton\nEste objeto no se mueve")
        exit()
    else:a=fuerzaNeta/m
else:
    a=fx/m
    if a==0:
        print("No se mueve")
if a<0:
    movimiento="<-"
elif a>0:
    movimiento="->"
print("El objeto tiene una aceleracion de",a,"m/s^2 y se mueve hacia ",movimiento)
#HOLA PROFE!
