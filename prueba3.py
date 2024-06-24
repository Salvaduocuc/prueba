def interfas_usuario():
    print("*"*35)
    print("*           MUNDO LIBRO           *")
    print("*"*35)
    
    lista_opciones = ["Mantenedor de libros", "Reportes","Salir"]
    for i in range(len(lista_opciones)):
        print(f"[{i+1}] - {lista_opciones[i]}")

def interfas_mantenedor_libros():
    print("*"*35)
    print("*           MUNDO LIBRO           *")
    print("*"*35)
    lista_opciones = ["Agregar libro","editar libro", "Eliminar libro","Buscar libro","Volver"]
    for i in range(len(lista_opciones)):
        print(f"[{i+1}] - {lista_opciones[i]}")






