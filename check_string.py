#simple system for checking if someone has written ANYTHING in a string
#not to check WHAT someone has written in a string

name = input("Enter your name... ")
name = bool(name)


if name == True:
    print("Go on.")
else:
    print("You have not entered anything. Try again.")