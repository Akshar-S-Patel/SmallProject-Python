import  random

random_number = random.randint(1, 101)
life = 10

print("Maximum Life = 10")
while life:
    print("Life :",life)
    val = int(input("\nEnter a number (1 - 100): "))
    if val > random_number:
        print("You Guess Too Large")
        life -= 1
    elif val < random_number:
        print("You Guess Too Less")
        life -= 1
    elif val == random_number:
        print("\nYeeee You Won" )
        print("Life Remaning :",life-1)
        break
else :
    print("\nGame Over\nYour life exhausted")


