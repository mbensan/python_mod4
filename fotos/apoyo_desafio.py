from error import DimensionError

class Foto():
  MAX = 2500

  def __init__(self, ancho: int, alto: int, ruta: str) -> None:
    if ancho > self.MAX or ancho < 1:
      raise DimensionError("La dimensión está mal", ancho, self.MAX)
    if alto > self.MAX or alto < 1:
      raise DimensionError("La dimensión está mal", alto, self.MAX)
    self.__ancho = ancho
    self.__alto = alto
    ruta = ruta

  @property
  def ancho(self) -> int:
    return self.__ancho

  @ancho.setter
  def ancho(self, ancho) -> None:
    if ancho > self.MAX or ancho < 1:
        raise DimensionError("La dimensión está mal", ancho, self.MAX)
    self.__ancho = ancho

  @property
  def alto(self) -> int:
    return self.__alto

  @alto.setter
  def alto(self, alto) -> None:
    if alto > self.MAX or alto < 1:
        raise DimensionError("La dimensión está mal", alto, self.MAX)
    self.__alto = alto


if __name__ == '__main__':
  while True:
    try:
      ancho = int(input('Ingrese el ancho de una foto: '))
      alto = int(input('Ingrese el alto de una foto: '))

      fotito = Foto(ancho, alto, '/assets/img/avatar.png')
    except DimensionError as e:
      print('error en la toma de datos')
      print(e)
      continue
    break

  print('Se genero la foto')