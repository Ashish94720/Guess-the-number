import random
if __name__ == '__main__':
    a = random.randint(0, 20)
    print("________________Game Start____________________")
    user_input = int(input("Please enter number between 0 to 20 : "))
    if abs(user_input - a) >= 5:
        print("You guess is too High")
    elif abs(a - user_input) >= 5:
        print("You guess is too Low")
    elif a == user_input:
        print("Congratulations ! You Guess is perfect")
    else:
        print("Your guessing is to close")
    print("Original number is {} ".format(a))
