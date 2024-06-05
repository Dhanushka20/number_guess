import random

#a number is guess

type_of_number = input("Type a number: ")

if type_of_number.isdigit():
    type_of_number = int(type_of_number)

    if type_of_number <= 0:
        print("Please enter a number more than '0'.")
        quit()
else:
    print("Pleae make sure that enter only number.")        

random_number = random.randint(0,type_of_number)

guesses = 0
is_continue  =True
while is_continue:
    guesses =+ 1
    user_input = input("User input: ")

    if user_input.isdigit():
        user_input = int(user_input)

    else:
        print("Pleae make sure that enter only number.")
        continue

    if user_input == random_number:
        print("You win! congratulations!")
        break

    elif user_input > random_number:
        print("You have entered above number")

    else:
        print("You have entered below number")

print("You got", guesses, "guesses.")        





