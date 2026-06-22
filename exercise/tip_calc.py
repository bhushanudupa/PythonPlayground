print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip_percent = float(input("How much tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))

tip_amount = total_bill * (tip_percent / 100)
total_amount_with_tip = total_bill + tip_amount
amount_per_person = total_amount_with_tip / num_people

final_amount = round(amount_per_person, 2)
print(f"Each person should pay: ${final_amount}")