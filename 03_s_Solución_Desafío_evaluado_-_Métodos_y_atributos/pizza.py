from ingredientes import proteicos, vegetales, masas

# Define la clase
class Pizza:
    # Agrega atributo tamaño
    tamanio = "familiar"

    # Agrega atributo precio
    precio = 10000

    @staticmethod
    def validar_elemento(solicitado, posibles):
        # Se usa operador in para validar que primer argumento se encuentre en el segundo
        # Como mejora se pasa el primer argumento a minúscula
        return solicitado.lower() in posibles

    def pedir(self):
        # Almacena proteico
        self.proteico = input("\nIngrese qué proteína desea."
        "Las posibilidades son:\n- Vacuno\n- Pollo\n- Carne vegetal\n")

        # Define atributo vegetales como lista
        self.vegetales = []
        
        # Almacena primer vegetal
        self.vegetales.append(input("\nIngrese el primer ingrediente"
        " vetegal. Las opciones son:\n-Tomate\n-Aceitunas\n-Champiñones\n"))

        # Almacena segundo vegetal
        self.vegetales.append(input("\nIngrese el segundo ingrediente "
        "vetegal.\n"))

        # Almacena tipo de masa
        self.tipo_de_masa = input("\nIngrese tipo de masa."
        "Las posibilidades son:\n- Tradicional\n- Delgada\n")

        self.es_una_pizza_valida = self.validar_elemento(self.proteico, proteicos) and \
            self.validar_elemento(self.vegetales[0], vegetales) and \
            self.validar_elemento(self.vegetales[1], vegetales) and \
            self.validar_elemento(self.tipo_de_masa, masas)
