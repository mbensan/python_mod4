class Medicamento:

  iva = 0.19

  def __init__(self, nombre, stock=0):
    self.nombre = nombre
    self.stock = stock
    # no dejar que un tercero modifique estas variables
    self.__precio_bruto = 0
    self.__precio_neto = 0
    self.__descto = 0.0
  
  def asignar_precio (self, valor):
    self.__precio_bruto = valor
    if valor >= 20000:
      self.__descto = 0.2
    elif valor >= 10000:
      self.__descto = 0.1
    self.__precio_neto = (self.__precio_bruto * (1 + Medicamento.iva)) * (1 - self.__descto)
  
  @property
  def precio_bruto(self):
    return self.__precio_bruto

  @property
  def precio_neto(self):
    return self.__precio_neto

  @property
  def descto(self):
    return self.__descto
  
  @descto.setter
  def descto(self, nuevo_valor):
    self.__descto = nuevo_valor

# OTRO ARCHIVO ...
m1 = Medicamento('Paracetamol', 5)
m2 = Medicamento('Eutirox')
# ejecutamos el método "asignar_precio"
m2.asignar_precio(13990)
print(m2.precio_neto)

