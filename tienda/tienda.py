from producto import Producto

# tipo = "supermercado" | "farmacia" | "restoran"
'''
-restoran al momento de agregar productos, el stock siempre es 0
-al momento de listar, los restoran y farmacia esconden el stock
-soupermercado muestran mensaje pocos disponibles si stock <= a 10
- farmacias agregan mensaje envio gratis si preico superior a 15000
'''
class Tienda:
  
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
  
  def listar_productos(self):
    pass

  def realizar_venta(self):
    pass