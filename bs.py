import random
brawlstars = int(input("kaç harf veya rakamlı olsun"))
kral = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
şifre = ""


for i in range(brawlstars):
    şifre += random.choice(kral)

print(şifre)
