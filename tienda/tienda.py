from abc import ABC, abstractmethod
from producto import Producto

# tipo = "supermercado" | "farmacia" | "restoran"
'''
-restoran al momento de agregar productos, el stock siempre es 0
-al momento de listar, los restoran y farmacia esconden el stock
-soupermercado muestran mensaje pocos disponibles si stock <= a 10
- farmacias agregan mensaje envio gratis si preico superior a 15000
'''
class Tienda(ABC):
  
  def __init__(self, nombre, costo_delivery):
    self.__nombre = nombre
    self.__costo_delivery = costo_delivery
    self.productos = []
  
  def ingresar_producto (self, nombre, precio, stock):

    nuevo_producto = Producto(nombre, precio, stock)
    for prod in self.productos:
      if prod == nuevo_producto:
        prod.stock += nuevo_producto.stock
        return
    # si llego a esta linea, quiere decir que nunca encontré el producto
    self.productos.append(nuevo_producto)
  @abstractmethod
  def listar_productos(self):
    pass

  def realizar_venta(self, nombre_buscado, cantidad_solicitada):
    for producto in self.productos:
      if producto.nombre == nombre_buscado and producto.stock >= cantidad_solicitada:
        print(f'Se vende {cantidad_solicitada} unidades del producto {producto.nombre}')
        producto.stock -= cantidad_solicitada
        return
    # si llegamos acá, el producto no existe o no hay stock suficiente
    print(f'No hay suficientes {nombre_buscado}')
