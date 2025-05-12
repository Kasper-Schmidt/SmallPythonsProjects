# Let's build a coffee shop together! We're going to build a coffee shop using some new Python Programming concepts!

# Let's build a robot barista!




print("Hello, welcome to Schmidt Coffee!")

name = input("What is your name?\n")

if name == "Ben":
    evil_status = input("Are you evil?\n")
    if evil_status == "Yes":
        print("You're not welcome here evil Ben! GET OUT!")
        exit()
    else:
        print("So you are one of those good Bens, Come in my friend!")

else:
    print("Hello " + name + ", Thanks you so much for coming in today.\n\n")

menu = "Black Coffee, Espresso, Latte, Cappucino, Frappucino"

print(name + ", What would you like from our menu today? Here is what we are serving:\n" + menu)

order = input().strip().title() # Sikrer at det virker uanset om det er lowercase eller uppercase

if order == "Frappucino":
    price = 8
elif order == "Black Coffee":
    price = 3
elif order == "Espresso":
    price = 4
elif order == "Latte":
    cream = input("Would you like Whipped Cream on that?\n")
    if cream == "Yes":
        print("We will get you that")
        price = 6
    else:
        print("Okay, No whipped cream for you my friend")
        price = 4
elif order == "Cappucino":
    price = 5
else:
    print("Sorry, we dont sell that here.")

amount = input("How many would you like?\n")

total = price * int(amount)

print("Sounds good " + name + ", we will have your " + amount + " " + order + " ready for you in a moment, the total price will be: $" + str(total))

