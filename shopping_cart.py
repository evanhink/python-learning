#print user instructions
print("""Welcome. This program allows for you to calculate how many of a single item you
are buying, then calculate the price of the total items.
First, input the name of the item you are buying, followed by price,
then quantity of item, then the program will calculate the total price in USD. ($)\n""")


#gather all information as described in user instructions
item_name = input("What is the name of the item you are buying?: \n")
item_quantity = int(input("Excellent. How many of this item are you buying?: \n"))
item_price = float(input("Finally, how much will this item cost in USD?: \n"))


#finally, calculate the total of all the items, then print the total result.
total_price = float(item_price * item_quantity)
print(f"You are buying {item_quantity}  {item_name}. The total cost comes out to \n")
print(total_price)
