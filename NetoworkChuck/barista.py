# Let's build a coffee shop together! We're going to build a coffee shop using some new Python Programming concepts!

# Let's build a robot barista!




print("Hello, welcome to Schmidt Coffee!")

name = input("What is your name?\n")

print("Hello " + name + ", Thanks you so much for coming in today.\n\n")

menu = "Black Coffee, Espresso, Latte, Cappucino"

print(name + ", What would you like from our menu today? Here is what we are serving:\n" + menu)

order = input()

price = 5

amount = input("How many would you like?\n")

total = price * int(amount)

print("Sounds good " + name + ", we will have your " + amount + " " + order + " ready for you in a moment, the total price will be: $" + str(total))

