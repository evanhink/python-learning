print("This program is for calculating the area of a 2 dimensional rectangle.")
print("The area of a rectangle is calculated with: area = length * width.\n")

#take the user's input to store a variable named length and width, then convert it
#to floating point numbers with the float() function

length = float(input("Enter length in centimeters: "))
width = float(input("Enter height in centimeters: "))


#taking the user's input of length and width, multiplying them, then printing
#the product with an f-string
area = (length * width)
print(f"The area of your rectangle is {area} cm².")
