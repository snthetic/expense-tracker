# Expense Tracker - Installment 2: Talking to the User
# Author: Seth Henri J. Suazo
# Asks for the user's name and two expenses, then prints a summary.

print("=" * 40)
print("\t\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)

print("\nMAIN MENU")
print("\t[1] Add an expense\t(coming soon)")
print("\t[2] View all expenses\t(coming soon)")
print("\t[3] Show total spent\t(coming soon)")
print("\t[4] Exit\t\t(coming soon)")
print()

name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.\n")

item1 = input("First expense? ")
amount1 = float(input("Amount? "))
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

total = amount1 + amount2
average = total / 2

print()
print("-" * 40)
print("SUMMARY")
print(f"  - {item1}:\t${amount1:.2f}")
print(f"  - {item2}:\t${amount2:.2f}")
print(f"Total spent:\t${total:.2f}")
print(f"Average:\t${average:.2f}")
print("-" * 40)
print("Made by: Seth Henri J. Suazo | Installment 2")