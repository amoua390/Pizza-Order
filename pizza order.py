print("Thank you for choosing Python Pizza Deliveries!")
print("What size pizza would you like? S, M, or L")
size = input() 
print("Do you want pepperoni? Y or N")
add_pepperoni = input() 
print("Do you want extra cheese? Y or N")
extra_cheese = input()

bill = 0

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill +=25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")

