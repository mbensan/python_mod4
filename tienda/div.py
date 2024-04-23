from colorama import Fore, Back, Style

class DivError(Exception):
  pass

def div(num1: str, num2: str) -> str:
  try:
    num1 = int(num1)
    num2 = int(num2)
    cuociente = num1 / num2
  except ValueError as error:
    # debug(error)
    raise DivError('Debe ingresar sólo números enteros')
  except ZeroDivisionError:
    raise DivError('No se puede dividir por Zero')

  return 'El resultado de la división es: ' + str(cuociente)


def interact ():
  while True:
    print(Style.RESET_ALL)
    num1 = input('Ingrese el dividendo (o "exit" para salir): ')
    if num1 == 'exit':
      break
    num2 = input('Ingrese el dividor: ')
    
    try:
      result = div(num1, num2)
      print(result)
    except DivError as e:
      print(Fore.RED + Back.BLACK, e)

interact()
