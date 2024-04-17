from tienda import Tienda
from producto import Producto

class Restoran(Tienda):

  def listar_productos(self):
    for p in self.productos:
      print(f'{p.nombre}, ${p.precio}')
  
  def ingresar_producto(self, nombre, precio):
    nuevo_producto = Producto(nombre, precio, 0)
    for prod in self.productos:
      if prod == nuevo_producto:
        return
    # si llego a esta linea, quiere decir que nunca encontré el producto
    self.productos.append(nuevo_producto)

