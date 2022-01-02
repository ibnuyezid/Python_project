import random
 
def guss(x):
    random_number=random.randint(1,x)
    
    gusse=0
    while gusse!=random_number:
        gusse=int(input(f"Enter a number between one and {x}: "))
        if gusse > random_number:
            print("too high, try again! ")
        elif gusse < random_number:
            print("too low, try again ! ")
    print(f"congra, you have got the number the secret number was {random_number} ")

guss(5)

 