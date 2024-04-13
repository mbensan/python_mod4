from abc import ABC, abstractmethod # abstract base class

class ACredito(ABC):
  @abstractmethod
  def definir_monto (self, valor):
    pass

  def mostrar_monto (self):
    return self.monto

class CredConsumo(ACredito):
  '''El monto debe ir entre 1M y 5M'''
  def __init__(self):
    self.monto = None
    self.email = None
  
  # modificar el monto
  def definir_monto(self, valor):
    if valor < 1000000:
      self.monto = 1000000
    elif valor > 5000000:
      self.monto = 5000000
    else:
      self.monto = valor

  def __str__(self):
    return f'Credito de Consumo de ${self.monto}'

class CredHipotecario(ACredito):
  '''El monto debe ir entre 20M y 100M'''
  def __init__(self):
    self.monto = None
    self.email = None
  
  # modificar el monto
  def definir_monto(self, valor):
    if valor > 100_000_000:
      self.monto = 100_000_000
    elif valor < 20_000_000:
      self.monto = 20_000_000
    else:
      self.monto = valor
  
  def __str__(self):
    return f'Crédito Hipótecario: ${self.monto}'

  # agregar un email


