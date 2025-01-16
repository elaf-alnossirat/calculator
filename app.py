number1 = int(input("enter the first number : "))
number2 = int(input("enter the second number : "))

print("the oparations you can use:")
print("(+) for addition")
print("(-) for subtraction")
print("(*) for multiplication")
print("(/) for division")

oparation = input("enter the oparation: ")


try:
  
  if oparation == "+":
    print('{}+{} '.format(number1 ,number2))
    print(number1 + number2)
  elif oparation == "-":
    print('{}-{} '.format(number1 ,number2))
    print(number1 - number2)  
  elif oparation == "*":
    print('{}*{} '.format(number1 ,number2))
    print(number1 * number2)    
  else:
    print('{}/{} '.format(number1 ,number2))
    print(number1 / number2)
    
except KeyboardInterrupt:
     print("kyboard interrupted") 