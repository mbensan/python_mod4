
class Saludador:
  # yo puedo recibir un número indefinido de parámetros
  #                  lista   diccionario
  def saludar (self, *args, **kwargs):
    for nombre in args:
      print('hola ' + nombre)
    
    for idioma, saludo in kwargs.items():
      print(f'En {idioma} se saluda con {saludo}')
    
# Universal Modelling Language
s = Saludador()
s.saludar('Cristian')
          #posicionales     # nombrados
s.saludar('Dani', 'Mario', sueco='Hej', frances='Bonjour', aleman='Hallo')
s.saludar('Fernando', 'Domi', 'Andres')
