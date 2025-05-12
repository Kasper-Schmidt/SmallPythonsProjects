# Velkomstbesked til kunden
print("Hello, welcome to Schmidt Coffee!")

# Spørger brugeren om deres navn
name = input("What is your name?\n")

# Hvis navnet er "Ben", tjekker vi om personen er ond
if name.strip().title() == "Ben":
    evil_status = input("Are you evil?\n")
    if evil_status.strip().lower() == "yes":
        print("You're not welcome here evil Ben! GET OUT!")
        exit()
    else:
        print("So you are one of those good Bens, come on in my friend!")
else:
    print(f"Hello {name}, thank you so much for coming in today.\n")

# Definerer menukortet med kaffe og basispriser
menu_prices = {
    "Black Coffee": 3,
    "Espresso": 4,
    "Latte": 4,         # Basispris uden flødeskum
    "Cappucino": 5,
    "Frappucino": 8
}

# Viser menukortet til kunden
print(f"{name}, what would you like from our menu today? Here is what we are serving:")
for item, price in menu_prices.items():
    print(f"- {item}: ${price}")

# Spørger kunden hvad de vil bestille og formaterer input korrekt
order = input("\nWhat would you like to order?\n").strip().title()

# Tjekker om ordren findes i menuen
if order not in menu_prices:
    print("Sorry, we don't sell that here.")
    exit()

# Særligt tjek hvis kunden vælger "Latte"
if order == "Latte":
    cream = input("Would you like Whipped Cream on that? (Yes/No)\n").strip().lower()
    if cream == "yes":
        print("We will get you that.")
        price = 6  # Pris med flødeskum
    else:
        print("Okay, no whipped cream for you my friend.")
        price = 4  # Basispris uden flødeskum
else:
    # Hvis det ikke er latte, bruges prisen fra menuen
    price = menu_prices[order]

# Spørger hvor mange kopper kunden vil have
amount = input("How many would you like?\n")

# Tjekker at mængden er et gyldigt tal
if not amount.isdigit() or int(amount) <= 0:
    print("Please enter a valid number greater than 0.")
    exit()

# Udregner totalprisen
total = price * int(amount)

# Bekræftelse og prisvisning
print(f"Sounds good {name}, we will have your {amount} {order}(s) ready shortly. Total price: ${total}")
