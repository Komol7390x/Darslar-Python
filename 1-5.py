import os
os.system("cls || clear")
class Employee:
    def __init__(self,name:str,family:str,data:str,dagre:str,salary:int):
        self.ism=name
        self.familya=family
        self.start=data
        self.lavozim=dagre
        self.oylik=salary
        self.bonus=self.oylik*1.25
    def info(self):
        print(f"Ismi: {self.ism}\nFamilya: {self.familya}\nIshga joylashgan vaqti: {self.start}")
        print(f"Lavozimi: {self.lavozim}\nOylik: {self.oylik} so'm")
    def bonus1(self):
        if self.oylik>=10_000_000:
            print("\nBonus qoshilmagan :(")
            print("------------------------")
        else:
            print("\nBonus qoshilgan :)")
            print(f"Bonus bilan: {self.bonus} so'm")
            print("------------------------")

user1=Employee("Adhmabek","Solihov","12.01.2022","Buxaltir",12_000_000)
user1.info()
user1.bonus1()

user2=Employee("Ravshabek","Bekov","14.10.2024","Oshpaz",7_500_000)
user2.info()
user2.bonus1()


# 5-masala. Employee(Hodim) nomli class yarating(ismi, familiyasi, ishga
# joylashgan sanasi, lavozimi, maoshi, bonusi kabi attributelar bilan). Maoshi
# 10_000_000 dan kam bo’lgan hodimlarga 25% bonus beruvchi metod
# yozing.
# Yani oylik= 8_000_000, bonus=2_000_000 kabi