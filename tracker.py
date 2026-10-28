# Expense Tracker - Installment 4: The Tracker Makes Decisions
# Author: Seth Henri J. Suazo
# Adds size messages, a two-big warning and a budget verdict.

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

subtotal = 0

item1 = input("First expense? ")
amount1 = float(input("Amount? "))
subtotal += amount1
if amount1 > 200:
    print("  Huge expense - are you sure?")
elif amount1 > 100:
    print("  Big expense.")
elif amount1 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal += amount2
if amount2 > 200:
    print("  Huge expense - are you sure?")
elif amount2 > 100:
    print("  Big expense.")
elif amount2 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

if amount1 > 100 and amount2 > 100:
    print("  Two big expenses in a row - slow down!")

average = subtotal / 2

tax_percent = float(input("Tax rate %? "))
tax = subtotal * tax_percent / 100
total = subtotal + tax

budget = float(input("Your budget? "))
over_budget = total > budget
left = budget - total

print()
print("-" * 40)
print("SUMMARY")
print(f"  - {item1}:\t${amount1:.2f}")
print(f"  - {item2}:\t${amount2:.2f}")
print(f"Subtotal:\t${subtotal:.2f}")
print(f"Average:\t${average:.2f}")
print(f"Tax ({tax_percent}%):\t${tax:.2f}")
print(f"Grand total:\t${total:.2f}")
if over_budget:
    print(f"Over budget by ${-left:.2f}!")
elif total > budget * 0.9:
    print(f"Careful: only ${left:.2f} left.")
else:
    print(f"Within budget. ${left:.2f} left.")
print("-" * 40)
print("Made by: Seth Henri J. Suazo | Installment 4")