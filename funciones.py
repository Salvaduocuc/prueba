import prueba3 
import json

salir = False

def usuario():
    usa = input(">>")
    return usa

def agregar_libro():
    with open("biblioteca.json","a") as agregar:
        h = agregar.write(usuario())

def editar_libro():
    with open("biblioteca.json","w") as agregar:
        print("Introdusca ID del librp que quieres editar:")
        
def eliminar():
    pass

def buscar_libro():
    with open("biblioteca.json","r") as agregar:
        leer = agregar.read()
        print(leer)

while salir == False:
    prueba3.interfas_usuario()
    usa = usuario()
    if usa == "3":
        salir = True
    if usa == "1":
        prueba3.interfas_mantenedor_libros()
        use = usuario()
        if use == "1":
            agregar_libro()
        if use == "4":
            buscar_libro()