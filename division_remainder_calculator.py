# user instructions
print("""Welcome, this program is designed to divide inputted numbers and return
a whole number alongside the remainder.
Step 1: Enter the first number you would like to divide.
Step 2: Enter the second number.""")

# get data from user input then convert it to int()
first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")

first_number = int(first_number)
second_number = int(second_number)

dividend = first_number // second_number
remainder = first_number % second_number

print(f"The dividend is {dividend} and your remainder is {remainder}.")

