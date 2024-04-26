from classes.carro import Carro
from classes.moto import Moto


carro1 = Carro("Toyota", "Corolla", 4)
carro2 = Carro("Ford", "Mustang", 2)
carro3 = Carro("Volkswagen", "Golf", 5)

moto1 = Moto("Honda", "CBR 1000RR", "Esportiva")
moto2 = Moto("Yamaha", "MT-07", "Naked")
moto3 = Moto("Kawasaki", "Ninja 650", "Esportiva")


def main():
    print(carro1)
    print(carro2)
    print(carro3)

    print(moto1)
    print(moto2)
    print(moto3)

if __name__ == '__main__':
    main()