#Programa en el que se definen la clase Animal y la clase Perro y Pajaro que heredan de Animal
class Animal:
    def __init__(self,patas,nombre):
        self.patas=patas
        self.nombre=nombre
    #metodo hacerRuido del animal
    def hacerRuido(self):
        pass

class Perro(Animal):
    def __init__(self,patas,nombre,raza):
        super().__init__(patas,nombre)
        self.raza=raza
    #metodo hacerRuido del perro
    def hacerRuido(self):
        print("Woof, woof")
    #metodo correr del perro
    def correr(self):
        print("Estoy corriendo")

class Pajaro(Animal):
     def __init__(self,patas,nombre):
        super().__init__(patas,nombre)
    #metodo hacerRuido del pajaro
     def hacerRuido(self):
        print("Tweet, tweet")
    #metodo volar del pajaro
     def volar(self):
        pass

if __name__=="__main__":
    perro=Perro(4,"Chucho","Labrador")
    perro.hacerRuido()
    perro.correr()