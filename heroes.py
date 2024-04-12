class Hero: 
    num_heroes = 0 #estatico ya que pertenece a la clase
    def __init__(self, name: str, health: int, power: int = 10):
        self.name = name
        self.health = health
        self.power = power
        self.hp = health
        self.bag = []
        Hero.num_heroes += 1
    
    @staticmethod #son como metodos generLES. NO REQUIERE INSTANCIA
    def print_num_heroes():
        print(f'En este momento tenemos {Hero.num_heroes} heroes')
    
    def gritar(self):
        print (f'BAZAAAAAAAAAAAAAIIIII!! Yo {self.name} te voy a matar!')
        
    def atack(self, victim):
        victim.hp -= self.power
        
    @staticmethod
    def is_dead(person_hp):
        if person_hp <= 0:
            return True
        else:
            return False
            
aragon = Hero('Aragon', 100, 10) #primera instancia
rayhar = Hero('Rayhar', 100, 12)
yamcha = Hero('Yamcha', 10, 2)

gohan = Hero('Gohan', 120)

aragon.gritar()
Hero.print_num_heroes()

aragon.atack(rayhar)
print(f'{rayhar.name} tiene {rayhar.hp} puntos de vida')

rayhar.atack(yamcha)
print(Hero.is_dead(yamcha.hp))

print(gohan.power)
