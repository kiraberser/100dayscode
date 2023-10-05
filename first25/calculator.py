from art import logo

def add(n1, n2):
  return n1 + n2 

def substract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  game = True
  while game:
    operation_symbol = input("Pick an operation: ")
    num2 = float   (input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    cont = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit': ")
    if cont == "n":
      game = False
      calculator()
    else:
      num1 = answer
      
calculator()
    