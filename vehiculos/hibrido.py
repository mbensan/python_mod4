from vehiculos import Vehiculo

class Electrodomestico:

  def __init__(self, mAh, bateria):
    self.mAh = mAh
    self.bateria = bateria


class Hibrido(Vehiculo, Electrodomestico):
  def __init__(self, modelo, motor, rendimiento, autom=False, mAh=5000, bateria='5000Watt'):
    #super().__init__(modelo, motor, rendimiento, autom)
    Vehiculo.__init__(self, modelo, motor, rendimiento, autom)
    Electrodomestico.__init__(self, mAh, bateria)
    self.mAh = min(mAh, 5000)
  
  def get_consumo(self, kms):
    cons_normal = super().get_consumo()
    return cons_normal * (1 - self.mAh/10000)