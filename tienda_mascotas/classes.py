class Mascota:

  def __init__(self, especie, precio, cantidad):
    self.especie = especie
    self.precio = precio
    self.cantidad = cantidad
  
  def get_monto_total(self):
    return self.precio * self.cantidad

  def __str__(self):
    return f'{self.especie.upper()}. Precio: ${self.precio} (nos quedan sólo {self.cantidad})'

  def __iadd__(self, otro_valor: int):
    # sobreescritura del operador +=
    self.cantidad += otro_valor
    return self

# TSun Zu (dividir para vencer)

class Tienda:

  def __init__(self, nombre_tienda):
    self.nombre_tienda = nombre_tienda
    self.inventario = []

  def add_mascota(self, especie, precio, cantidad):
    nueva_mascota = Mascota(especie, precio, cantidad)
    self.inventario.append(nueva_mascota)

  def vender(self, nombre_especie):
    for mascota in self.inventario:
      if mascota.especie == nombre_especie:
        # si encuentro la mascota
        if mascota.cantidad > 0:
          mascota.cantidad -= 1
        else:
          print(f'No nos quedan {nombre_especie}')
        return
    print('No vendemos esa especie')

  def get_activos_mascotas(self):
    # todo el dinero que tengo en mascotas
    total = 0
    for mascota in self.inventario:
      total += mascota.get_monto_total()
    return total

  def mostrar_inventario(self):
    for mascota in self.inventario:
      print(mascota)

if __name__ == '__main__':

  alpaca = Mascota('Alpacas', 100000, 2)
  alpaca += 1
  print(alpaca)

  tienda1 = Tienda('Pikachu Store')
  tienda1.add_mascota('Tortuga Marina', 10000, 10)
  tienda1.add_mascota('Loro', 2000, 5)
  tienda1.add_mascota('Perro', 1000, 5)

  tienda1.vender('Loro')
  tienda1.vender('Avestruz')

  tienda1.mostrar_inventario()


class Dueño:

  def __init__(self, nombre, edad, especie, precio, cantidad):
    self.nombre = nombre
    self.edad = edad
    self.mascota = Mascota(especie, precio, cantidad)