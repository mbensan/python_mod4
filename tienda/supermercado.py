from tienda import Tienda
class Supermercado(Tienda):

  def listar_productos(self):
    for p in self.productos:
      if p.stock <= 10:
        print(f'{p.nombre}, ${p.precio}, Unidades: {p.stock} POCAS UNIDADES DISPONIBLES')
      else:
        print(f'{p.nombre}, ${p.precio}, Unidades: {p.stock}')
      

if __name__ == '__main__':           
  m = Supermercado('Ekono', 1500)
  m.ingresar_producto('Atún enlatado', 1400, 300)
  m.ingresar_producto('Papel higienico', 5000, 8)
  #print(m.productos)
  m.listar_productos()