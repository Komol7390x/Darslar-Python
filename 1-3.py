import os
os.system("cls || clear")
from itertools import zip_longest
class User: 
    def __init__(self,name,username):
        self.name=name
        self.username=username
        self.followers=[]
        self.following=[]
    
    def info(self):
        print(f"Name: {self.name}\nUsername: {self.username}\n")
        print("   Follower",2*"\t","Following\n")
        i=1
        for x,y in zip_longest(self.followers,self.following,fillvalue=1*"\t"):     
            print(i+1,".",x,end=" ")
            print(2*"\t",i+1,".",y)
            i+=1
    def follow(self,ism1):
            if ism1 not in self.following:
                self.following.append(ism1)
            else:print(f"\n{ism1} foydalanuvchi bor")
    
    def follower(self,ism2):
            if ism2 not in self.followers:
                self.followers.append(ism2)
            else:print(f"\n{ism2} foydalanuvchi bor")
    
    def unfollow(self,ism3):
        if ism3 in self.following:
            self.following.remove(ism3)
        else:print(f"\n{ism3} foydalanuvchi yoq")
    
    def remove_follower(self,ism4):
        if ism4 in self.followers:
            self.followers.remove(ism4)
        else:print(f"\n{ism4} foydalanuvchi yoq")

users=User("Will Smith","@_willsmith2")
name1=("Jack","Harry","Jacob","Charlie","Thomas","George","Oscar")
name2=("Lorenzo","Leonardo","Chiara","Isabella","Mia  ","Sophia","Corleone")
for i in range(len(name1)):
    users.follow(name1[i])
    users.follower(name2[i])
users.info()
print(f"\n\n1.Following yangi element qo'shish.\n2.Followingdan element o'chirish.\n3.Followersdan element o'chirish.")
try:
    son=int(input(">>> "))
except:print("Xato kiritish")
else:
    if son==1:
        ism=input("Ism kiriitng: ")
        users.follow(ism)
    elif son==2:
        ism=input("Ism kiriitng: ")
        users.unfollow(ism)
    elif son==3:
        ism=input("Ism kiriitng: ")
        users.remove_follower(ism)
    else: print("Xato kiritish")

print("\n")
users.info()
    
        
# 3-masala. User(Foydalanuvchi) nomli class yarating(name, username,
# followers (list), following (list) kabi attributelari bilan). Bu classga follow
# (followingga yangi element qo’shish), unfollow (followingdan element
# o’chirish) va remove_follower(followersdan element o’chirish) nomli
# metodlar yozing.
