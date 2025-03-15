#ask for user input
#used float data type to accomodate both whole and decimal inputs

num1 = float(input("Enter the first number: ")) 

num2 = float(input("Enter the second number: "))  

operator = input("Please enter an arithmetic operator '+', '-', '*', '/': ")


# Carry out the mathematical operation of the operators 

if operator == '+' :
    result = num1 + num2

elif operator == '-':
    result = num1 - num2

elif operator == '*':
    result = num1 * num2


#To check if the second number is zero avoid zero errors 
elif operator == '/':
    
     if num2 != 0 :
        result = num1 / num2

     else :
      result = "Error: Division by zero is not allowed."

    
#Print the final result after the operation of the operators

print(f"{num1} {operator} {num2} = {result}")
