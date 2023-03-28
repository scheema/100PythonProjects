#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

total_bill = float(input('Please enter the total bill amount: '))
number_of_people = int(input('Please enter the number of people the total bill need to be split: '))
tip_percent = float(input('Please enter the tip amount %:  '))

per_person_amount = float( total_bill / (number_of_people ) * (1 + tip_percent * 0.01) )
formatted_per_person_amount = format(per_person_amount, '.2f')

print(f'The amount each person owes is : {formatted_per_person_amount}')
print(f'The amount each person owes is : {per_person_amount:.2f}')