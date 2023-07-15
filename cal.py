#TODO: Write the functions for arithmatic operations here
#These functions should cover Task 2
def calc(oprator,fNumber,sNumber):
  if oprator == '+':
    result = fNumber + sNumber
  elif oprator == '-':
    result = fNumber - sNumber
  elif oprator == '*':
    result = fNumber * sNumber
  elif oprator == '/':
    if sNumber == 0:
      result = "None"
      print("float division by zero")
    else:
      result = fNumber / sNumber
  elif oprator == '^':
    result = fNumber ** sNumber
  elif oprator == '%':
    result = fNumber % sNumber
  else:
    return print("Unrecognized operation")
  return print ("{0} {1} {2} = {3}" .format(fNumber, oprator, sNumber, result))

#-------------------------------------
#TODO: Write the select_op(choice) function here
#This function sould cover Task 1 (Section 2) and Task 3
def select_op(choice):
  if choice == '#' :
    return -1
  
  fNumber = input("Enter first number: ")
  print(fNumber)
  try:
    fNumber = float(fNumber)
  except:
    if fNumber == '#':
      return -1
    elif fNumber[-1] == '$':
      return
    else:
      print("Not a valid number,please enter again")
      return
  sNumber = input("Enter second number: ")
  print(sNumber)
  try:
    sNumber = float(sNumber)
  except:
    if sNumber == '#':
      return -1
    elif sNumber[-1] == '$':
      return
    else:
      print("Not a valid number,please enter again")
      return
  return calc(choice,fNumber,sNumber)
  



#End the select_op(choice) function here
#-------------------------------------
#This is the main loop. It covers Task 1 (Section 1)
#YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  if(select_op(choice) == -1):
    #program ends here
    print("Done. Terminating")
    exit()