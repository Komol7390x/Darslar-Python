import os
os.system("cls || clear")
class Telefon:
    def __init__(self,br,mod,pr,yil):
        self.brend=br
        self.model=mod
        self.narx=pr
        self.yili=yil
    def update_price(self,price:int):
        self.narx=price
    def info(self):
        print(f"Brand: {self.brend}\nModel: {self.model}\nNarx: {self.narx} $\nYil: {self.yili} yili")
user=Telefon("Apple ","IPhone 16 Pro Max",800,2024)
user.info()
try:
    son=int(input("\nYangi narxni kiriitng: "))
except:print("\nXato kiriitingiz!!!")
else:
    user.update_price(son)
finally:
    print("\n")
    user.info()
# 4-masala. Phone(Telefon) nomli class yarting(brand, model, narx, yili kabi
# attributelar bilan). Bu classga narxni o’zgartirish uchun update_price nomli
# metod yozing.