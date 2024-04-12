from vehiculos import Vehiculo
# lista de instancias de la clase Vehiculo
mis_vehiculos = []

# 1. Ciclo infinito para ir llenando la lista
while True:
    # 1. Pedimos los datos del nuevo vehículo
    modelo = input('Ingrese el modelo: ')
    if modelo == '0':
        break
    motor = float(input('Ingrese la cilindrada del motor: '))
    rendimiento = float(input('Ingrese el rendimiento de su vehículo (Kms/Lt) '))
    autom = input('¿Es automático? (si | no) ')
    # 2. Transformamos la variable autom
    autom = True if autom == 'si' else False
    # 3. Creamos la instancia
    auto_nuevo = Vehiculo(modelo, motor, rendimiento, autom)
    # 4. Lo agregamos a la lista
    mis_vehiculos.append(auto_nuevo)

for auto in mis_vehiculos:
    auto_automatico = 'SI' if auto.automatico else 'NO'
    print(f'Tengo un {auto.modelo} que es automático {auto_automatico}')
