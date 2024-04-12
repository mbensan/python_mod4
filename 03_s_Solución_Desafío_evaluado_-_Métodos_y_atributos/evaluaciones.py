from pizza import Pizza

# a:
print("Todas las pizzas tienen un tamaño {} y un valor de {}".format(
    Pizza.tamanio, Pizza.precio
))

# b:
print(Pizza.validar_elemento("salsa de tomate", ["salsa de tomate", "salsa bbq"]))

# c:
pizza = Pizza()
pizza.pedir()

# d:
print("\nVegetales: {}\nProteína: {}\nTipo de masa: {}\n¿Es una pizza válida?: {}\n".format(
    pizza.vegetales, pizza.proteico, pizza.tipo_de_masa, pizza.es_una_pizza_valida
))

# e:
print("¿La clase es una pizza válida?: {}".format(Pizza.es_una_pizza_valida))