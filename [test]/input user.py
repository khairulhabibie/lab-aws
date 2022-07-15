## if, elif, and else statement
try :
    bananas = int(input("how many bananas do you have: "))
    if bananas >= 5:
        print("You have a bunch of bananas")
    elif bananas in range (1,5):
        print("You have small bunch of bananas")
    elif bananas == 0:
        print("You have no bananas")
    else:
        print("You don't have bananas, you borrow {} bananas".format(bananas))
except ValueError: 
    print("Input must be in numeric form!")
