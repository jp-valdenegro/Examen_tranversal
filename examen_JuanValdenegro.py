import random
trabajadores=["Juan Perez","Maria Garcia","Carlos Lopez","Ana Martinez","Pedro Rodriguez","Laura Hernandez","Miguel Sanchez","Isabel Gomez","Francisco Dias","Elena Fernandez"]
lista_sueldos=[]
def sueldos_random():
    aaaa=10
    while aaaa!=0:
        sueldos= random.randint(300000,2500000,)
        lista_sueldos.append(sueldos)
        aaaa-=1
        continue
    for fila in lista_sueldos:
        print(fila)
    for fila in trabajadores:
        print(fila)

def salir():
    print("Finalizando el Programa \nDesarollado por Juan Valdenegro \nRUT 22.072.965-6")
    
while True:
    try:
        menu=int(input("Elija la opcion a realizar: \n1:Asignar sueldo  \n5:Salir del programa\n"))
        if menu ==1:
            sueldosrandom=sueldos_random()
            print(sueldosrandom)
        elif menu==5:
            salirrr=salir()
            print(salirrr)
        else:
            print("la opcion ingresada no existe")
            break
    except ValueError:
        print("ERROR, INTENTE DE NUEVO")
        continue
    
    