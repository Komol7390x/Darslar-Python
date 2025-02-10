import os

class Avto:
    def __init__(self,nomi,rangi,narxi,probeg,tezlik):
        self.nomi=nomi
        self.rangi=rangi
        self.narxi=narxi
        self.probeg=probeg
        self.tezlik=tezlik
    def info(self):
        print(f"Nomi: {self.nomi}\nRangi: {self.rangi}")
        print(f"Narxi: {self.narxi} $\nProbeg: {self.probeg} km\nTezlik: {self.tezlik} km/s")
    def update_probeg(self,son):
        self.probeg+=son
        print("Probeg yangilandi :)\n")
    def update_narx(self,son):
        self.narxi+=son
        print("Narx yangilandi !\n")
        
os.system("cls || clear")
print("      INFO\n")
user=Avto("Nexia","OQ",9_000_000,50_000,200)
user.info()
print("\n1.Probegni oshiriish\n2.Narxini oshirish")
try:
    n=int(input(">>> "))
except:print("Kiriitshda xatolik !")
else:
    if n==1:
        son=int(input("\nProbegini qanchaga oshirasiz: "))
        user.update_probeg(son)
        user.info()
    elif n==2:
        son=int(input("\nNarxini qanchaga oshirasiz: "))
        user.update_narx(son)
        user.info()
    else:print("Xato son kiritingiz!")

# 1-masala. Avto nomli class yarating(nomi, rangi, narxi, probegi, tezligi kabi
# attributelar bilan). Bu classga probegni o’zgartirish uchun update_probeg
# va narxni o’zgartirish uchun update_narx nomli metodlar qo’shing.
