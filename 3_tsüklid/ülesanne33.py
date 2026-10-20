from random import randint
salajane = randint(1,10)
print("Arva arv 1-10" )
pakkumine = int(input())
while pakkumine != salajane:
    if salajane > pakkumine:
        print("Salajane arv on suurem")
    else:
        print("Salajane arv on väiksem")
    print("Arva arv 1-10")
    pakkumine = int(input())
print("Õige!")