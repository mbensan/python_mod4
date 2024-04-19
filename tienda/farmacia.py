from tienda import Tienda

class Farmacia(Tienda):

  def listar_productos(self):
    for p in self.productos:
      if p.precio > 15000:
        print(f'{p.nombre}, ${p.precio} ENVIOS GRATIS!!!')
      else:
        print(f'{p.nombre}, ${p.precio}')
  
  def realizar_venta(self, nombre_buscado, cantidad_solicitada):
    if (cantidad_solicitada > 3):
      print('Por ley, no podemos vender más de 3 unidades')
      return
    super().realizar_venta(nombre_buscado, cantidad_solicitada)

if __name__ == '__main__':
  salco = Farmacia('LadronBrand', 10000)
  salco.ingresar_producto('Querantol 20 Crema Ligera', 29870, 20)
  salco.ingresar_producto('ZInlergia 10 GEL', 12990, 0)

  salco.listar_productos()