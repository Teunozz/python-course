# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇
print("Welcome to the tip calculator!")

total = float(input("What was the total bill?\n$"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
number_of_people = int(input("How many people to split the bill?\n"))

total += total * (tip_percentage / 100)
cost_per_person = round(total / number_of_people, 2)

print("Each person should pay: {:.2f}".format(cost_per_person))
