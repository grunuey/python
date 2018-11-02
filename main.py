#calculator start message
print("My first python program : Calculator")
print("Select a number through 1~7 to choose a function.")
print("(1)add (2)multiply (3)subtract (4)divide (5)remainder (6)hexagonal (7)integ")

#user input
n=input('> ')

#input result message
base="You entered function number {}."
result=base.format(n)
print(result)
