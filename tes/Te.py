class Te:

  duracion = 365

  @staticmethod
  def instrucciones (tipo_te: str):
    '''tipo_te = "1" Te negro
       tipo_te = "2" Te verde
       tipo_te = "3" Infusión'''
    if tipo_te == '1':
      return 3, "Se recomienda tomar en la mañana"
    elif tipo_te == '2':
      return 5, 'Se recomienda tomar con el almuerzo'
    else:
      return 6, 'Se recomienda tomar al atardecer'
  
  @staticmethod
  def get_precio (peso):
    if peso == 300:
      return 3000
    else: # peso == 500
      return 5000
