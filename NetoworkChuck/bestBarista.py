# Velkomstbesked til kunden
print("Hello, welcome to Schmidt Coffee!")

# Spørger brugeren om deres navn
name = input("What is your name?\n")

# Hvis navnet er "Ben", tjekker vi om personen er ond
if name.strip().title() == "Ben":
    evil_status = input("Are you evil?\n")
    if evil_status.strip().lower() == "yes":
        # Hvis Ben er ond, bliver han smidt ud
        print("You're not welcome here evil Ben! GET OUT!")
        exit()
    else:
        # Hvis Ben ikke er ond, byder vi ham velkommen
        print("So you are one of those good Bens, come on in my friend!")
else:
    # Hvis det ikke er Ben, byder vi kunden almindeligt velkommen
    print(f"Hello {name}, thank you so much for coming in today.\n")

# Definerer menukortet med kaffe og tilhørende priser
menu_prices = {
    "Black Coffee": 5,
    "Espresso": 6,
    "Latte": 7,
    "Cappucino": 7,
    "Frappucino": 8
}

# Viser menukortet til kunden
print(f"{name}, what would you like from our menu today? Here is what we are serving:")
for item, price in menu_prices.items():
    print(f"- {item}: ${price}")

# Spørger brugeren, hvad de gerne vil bestille, og sørger for korrekt formatering
order = input("\nWhat would you like to order?\n").strip().title()

# Tjekker om ordren findes i menuen
if order in menu_prices:
    price = menu_prices[order]
else:
    # Hvis ordren ikke findes, afbryder vi programmet
    print("Sorry, we don't have that.")
    exit()

# Spørger hvor mange kopper brugeren gerne vil have
amount = input("How many would you like?\n")

# Tjekker om mængden er et gyldigt tal større end 0
if not amount.isdigit() or int(amount) <= 0:
    print("Please enter a valid number greater than 0.")
    exit()

# Udregner totalprisen for ordren
total = price * int(amount)

# Giver brugeren en bekræftelse og totalprisen
print(f"Sounds good {name}, we will have your {amount} {order}(s) ready shortly. Total price: ${total}")
