#1. Write a program that takes two numbers as inputs and displays their sum, product and quotient.
number_one = int(input("Enter your first number: "))
number_two = int(input("Enter your second number: "))

sum = number_one + number_two 
print(f"The sum of {number_one} and {number_two} is: {sum}")

product = number_one * number_two
print(f"The product of {number_one} and {number_two} is: {product}")

quotient = number_one / number_two
print(f"The quotient of {number_one} and {number_two} is: {quotient}")

#2. Write a program that compares two integers, print whether the first number is greater, less than or equal to the second number.
if number_one > number_two :
    print(f"{number_one} is greater than {number_two}")

elif number_one < number_two :
    print(f"{number_one} is less than {number_two}")

else :
    print(f"They are equal.")

#3. Write a program that checks if a given number is between 10 and 20, where 'Twenty is inclusive' using logical operators.
number = int(input("Enter an integer: "))

if 10 < number <= 20 :
    print(f"{number} is between 10 and 20, where twenty is inclusive.")
  
else :
    print(f"{number} is not between 10 and 20, where twenty is inclusive.")

#4. Write a program that prints integers from one to ten using a for loop.
for x in range(1,11) :
   print(x)
  
