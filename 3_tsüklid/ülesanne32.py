from random import randint
salajane = randint(1,10)
print("Arva arv 1-10" )
pakkumine = int(input())
while pakkumine != salajane:
    print("Vale!")
    print("Arva arv 1-10")
    pakkumine = int(input())
print("Õige!")