# Jason Rideout
# Project 1
# Rental Car Draft
# July 17, 2018

import sys

'''
Section 1: Collect customer input
'''

# Assignment of string input to variable rentalCode
rentalCode = input("(B)udget, (D)aily, or (W)eekly rental?\n")

# This if statement is a branching statement that allows for the correct prompt.
# If the rental code is weekly, the prompt asks for the number of weeks.
# The other two cases (budget and daily) are handled with the else statement, as they both count days, not weeks.
if rentalCode == "W":
  rentalPeriod = input("Number of Weeks Rented:\n") # The input string is assigned to the variable rentalPeriod
else:
  rentalPeriod = input("Number of Days Rented:\n")
rentalPeriod = int(rentalPeriod) # Change the value of rentalPeriod from a string to an integer

# Cost declarations for use in calculating the baseCharge
budgetCharge = 40.00
dailyCharge = 60.00
weeklyCharge = 190.00	

# Calculate charge depending on rentalCode
# Because only one rental code is possible at a time, the branching statement elif (else if) is used.
# This allows for more efficiency. If I had used all if statements, all three possibilities would be checked even if the first statement was true.
# I included an else branch in case an invalid code was entered by the user.
if rentalCode == "B":
  baseCharge = float(rentalPeriod) * budgetCharge # The variable rentalPeriod is accessed.
elif rentalCode == "D":
  baseCharge = float(rentalPeriod) * dailyCharge
elif rentalCode == "W":
  baseCharge = float(rentalPeriod) * weeklyCharge
else:
  baseCharge = 0
  print("Error: Invalid rentalCode.")

# Collect Mileage information
odoStart = input("Starting Odometer Reading:\n")
odoEnd = input("Ending Odometer Reading:\n")


'''
Section 2: Calculate the costs from the customer input
'''

# Calculate total miles
totalMiles = int(odoEnd) - int(odoStart)

# Budget cost is a flat charge per mile
if rentalCode == "B":
    mileCharge = float(totalMiles) * 0.25
# Daily cost is a flat charge ($0.25) per mile over 100 miles (averaged over rental duration) per day.
elif rentalCode == "D":
    averageDayMiles = totalMiles/rentalPeriod
    if averageDayMiles <= 100:
        extraMiles = 0
    else:
        extraMiles = averageDayMiles - 100
    mileCharge = extraMiles * 0.25 * rentalPeriod
# Weekly cost is a flat charge ($100) per day if the average weekly distance is over 900 miles.
elif rentalCode == "W":
    averageWeekMiles = totalMiles/rentalPeriod # The variables totalMiles is divided by rentalPeriod with the appropriate operator and assigned to averageWeekMiles
    if averageWeekMiles > 900:
        mileCharge = 100 * rentalPeriod
    else:
        mileCharge = 0

'''
Section 3: Display the results to the customer
'''

# Get total amount due and print out summary
amtDue = baseCharge + mileCharge

print("Rental Summary")
print("Rental Code:       ",rentalCode)
print("Rental Period:     ",rentalPeriod)
print("Starting Odometer: ",odoStart)
print("Ending Odometer:   ",odoEnd)
print("Miles Driven:      ",totalMiles)
print("Amount Due:        $%.2f" % amtDue) # The variable amtDue is limited to 2 digits past the decimal
