'''
Voy a realizar un ciclo infinito
En cada iteracion pregunto lo siguiente:
    - nombre de la especie
    - precio de la unidad
    - cantidad de ejemplares

Si el usuario ingresa como nombre de la especie un "0", entonces
termina el ciclo. Imprimo la lista de todas las mascotas

BONUS: Una vez finalizado el ciclo, imprimir el total de $ en especies
'''
print('Bienvenido al ADMIN de la tienda de mascotas')

def tienda ():
    mascotas = []

    while True:
        # 1. Pedimos los 3 datos de cada tipo de mascota
        especie = input('Ingrese la nueva especie:\n')
        # revisamos de inmediato si el usuario no desea agregar más mascotas
        if especie == '0':
            break
        precio = int(input('Ingrese el precio por ejemplar:\n'))
        cantidad = input('Ingrese el número de ejemplares:\n')

        cantidad = int(cantidad)
        # 2. armamos nuestro diccionario
        nueva_mascota = {
            'especie': especie,
            'precio': precio,
            'cantidad': cantidad
        }
        # 3. Agregamos el diccionario a la lista de mascotas
        mascotas.append(nueva_mascota)
    # 4. Ahora imprimimos todas las mascotas
    print(mascotas)

    # 5. Calculamos el total de $ en el inventario
    total = 0
    for mascota in mascotas:
        total += mascota['precio'] * mascota['cantidad']
    
    print(f'En la tienda hay ${total} en especies')
    


tienda()
