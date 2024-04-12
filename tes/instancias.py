from Te import Te

te1 = Te()
te2 = Te()

if type(te1) == type(te2):
    print('Ambos tipos de dato son iguales')


tiempo_preparacion, recomendacion = Te.instrucciones('2')
