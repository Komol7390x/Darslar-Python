import os
os.system("cls || clear")
class Restoran:
    def __init__(self,st,fn):
        self.start=st
        self.finish=fn
        self.menu={}
    def info(self):
        print(f"\nIsh vaqti: {self.start}-{self.finish}\n")
        print("         MENU\n")
        n=1
        for i in self.menu:
            print(n,". ",i,"-",self.menu[i],"so'm")
            n+=1
    def update_menu(self,nomi:str,narxi:int):
        n=nomi.lower()
        n=nomi.title()
        #maxsulot yoq bosa qoshadi
        if n not in self.menu:
            self.menu[n]=narxi
        else:
            os.system("cls || clear")
            print("\nBu maxsulot bor !!!\n")

user=Restoran("09:00","21:00")
menu={
    "Osh":30_000,
    "Dolma":25_000,
    "Lagman":33_000,
    "Assarti":45_000,
    "Bishteks":50_000
}
for i,m in menu.items():
    user.update_menu(i,m)
user.info()
try:
    m_nomi=input("\nNomini kiriitng: ")
    m_narx=int(input("Narxini kiriitng: "))
except:
    os.system("cls || clear")
    #xato kiritish bosa kod buzulib ketmiydi
    print("\nXatolik bor :)\n")
else:
    user.update_menu(m_nomi,m_narx)
finally:
    user.info()

# 2-masala. Restoran nomli class yarating(Ish vaqti, menyusi kabi
# attributelar bilan). Bu classga menyuga yangi ovqat qo’shi uchun metod
# yozing.