class Pelota:

  def __init__(self, color: str, tamaño: int = 5):
    self.color = color
    self.tamaño = tamaño
  
  @property
  def color_tamaño (self):
    return f'La pelota {self.color} es de tamaño {self.tamaño}'


p1 = Pelota('Naranja')
print( p1.color_tamaño )



# Ahora veremos para qué se usa property
class Termometro:

  def __init__(self, celsius):
    # atributo privado
    self.__celsius = celsius
  
  # getter
  @property
  def celsius(self):
    if self.__celsius > 100:
      return 'No vaya, se va a morir'
    return self.__celsius
  
  # setter
  @celsius.setter
  def celsius (self, temp):
    if temp < 273:
      print('No se puede bajar de los -273.15°C')
      return
    self.__celsius = temp
  
  def farenheit(self):
    return (self.__celsius * 1.8) + 32

t1 = Termometro(30)
t1.celsius = 300
print(t1.celsius)