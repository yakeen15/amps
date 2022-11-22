print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill? "))
per_tip = tip/100
total = (bill+per_tip)/split
rounded_total = round(total,2)
print("Each person should pay: $",rounded_total)