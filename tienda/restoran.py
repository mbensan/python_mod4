from tienda import Tienda
from producto import Producto

class Restoran(Tienda):

  def listar_productos(self):
    for p in self.productos:
      print(f'{p.nombre}, ${p.precio}')
  
  def ingresar_producto(self, nombre, precio, stock):
    nuevo_producto = Producto(nombre, precio, 0)
    for prod in self.productos:
      if prod == nuevo_producto:
        return
    # si llego a esta linea, quiere decir que nunca encontré el producto
    self.productos.append(nuevo_producto)
  
  def realizar_venta(self, nombre_buscado, cantidad_solicitada=None):
    for prod in self.productos:
      if prod.nombre == nombre_buscado:
        print(f'Saale un {nombre_buscado} maestro')
        return
    print('Ese plato no lo trabajamos')

