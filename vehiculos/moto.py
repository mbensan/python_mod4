from vehiculos import Vehiculo

class Moto(Vehiculo):
  # como extra, las motos pueden tener carrito
  def __init__(self, modelo, motor, rendimiento, autom=False, carrito=False):
    # toda la pega de la clase madre
    super().__init__(modelo, motor, rendimiento, autom)
    # las variables explusivas de la clase hija
    self.carrito = carrito
  
  def get_consumo(self, kms):
    consumo_normal = super().get_consumo(kms)
    if self.carrito:
      return consumo_normal * 1.3
    else:
      return consumo_normal


if __name__ == '__main__':
  gastadora = Moto('BMW GS310', 300, 30, carrito=True)

  print(gastadora.get_consumo(60))
  print(gastadora.calcular_gasto(60, 1000))
  print(isinstance(gastadora, Moto))
  print(isinstance(gastadora, Vehiculo))

