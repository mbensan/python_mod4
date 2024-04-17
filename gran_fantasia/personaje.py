import random

prob_soy_mejor = ['gana', 'gana', 'pierde']
prob_soy_peor = ['gana', 'pierde', 'pierde']
prob_soy_igual = ['gana', 'pierde']

class Personaje:

  def __init__(self, nombre):
    self.nombre = nombre
    self.__nivel = 1
    self.__exp = 0
  
  def get_estado(self):
    return f'{self.nombre} NIVEL: {self.__nivel} exp: {self.__exp}'
  
  # nivel 3   exp 10 (-60)
  
  def set_estado (self, ptos_exp):
    nueva_exp = self.__exp + ptos_exp

    if nueva_exp < 0:
      import pdb; pdb.set_trace()
      niveles_por_bajar = 1 + (nueva_exp // 100)
      self.__nivel = self.__nivel - niveles_por_bajar
      
      if self.__nivel < 1:
        self.__nivel = 1
      self.__exp = max(0, 100 + nueva_exp)
    else:
      self.__exp = nueva_exp % 100
      self.__nivel += nueva_exp // 100

  def __gt__(self, otro_personaje):
    # greather than (>)
    if self.__nivel > otro_personaje.__nivel:
      return True
    else:
      return False
  
  def __lt__(self, otro_personaje):
    # lesser than
    if self.__nivel < otro_personaje.__nivel:
      return True
    else:
      return False
  
  def atacar (self, otro):
    if self > otro:
      return random.choice(prob_soy_mejor)
    elif self < otro:
      return random.choice(prob_soy_peor)
    else: # niveles iguales
      return random.choice(prob_soy_igual)


p1 = Personaje('Pedro')
p2 = Personaje('Maria')

p1.set_estado(50)
p1.set_estado(50)
p1.set_estado(-30)
print(p1.get_estado())

'''
__gte__ (greather or equal than) >=
__eq__ (equals) ==
__str__
__init__
'''
