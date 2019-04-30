import datetime
import random
import time

# Get current time
now=datetime.datetime.now()
seconds=now.second
minutes=now.minute
hours=now.hour


# Calculate the result by applying first operator on two first operands
def firstOperator(op1,op2,operator):
 if operator == 1:
     op12 = op1 + op2
     operatorChar="+"
 elif operator == 2:
     op12 = op1 - op2
     operatorChar = "-"
 elif operator == 3:
     op12 = op1 * op2
     operatorChar = "*"
 elif operator == 4:
     op12 = op1 / op2
     operatorChar = "/"
 return  op12, operatorChar


# Turtle graphics
from turtle import *
turtle=Turtle(visible=False)
turtle.screen.title("CLOCK!")
turtle.screen.setup (width=800, height=700, startx=200, starty=0)
turtle.pencolor("red")
turtle.screen.bgcolor("#000000")

# Set values for HOUR
# Set first and second operands for HOUR
Hr_1 = random.randint(1, 9)
Hr_2 = random.randint(1, 9)

# Set first operator (+,-,*,/)
operatorHr1 = random.randint(1, 4)

# Calculate the result of two first operands for HOUR
op12Hr, operatorCharHr = firstOperator(Hr_1, Hr_2, operatorHr1)

# Find third operand based on two first operands for HOUR
Hr_3 = hours - op12Hr
Hr_3 = round(Hr_3, 2)

# Set second operator to "+"
operatorChar2Hr="+"
# Eliminate the second operator if the third operand is negative
if Hr_3 < 0:
 operatorChar2Hr = ""

# Set values for MINUTE
# Process is the same!
Min_1 = random.randint(1, 9)
Min_2 = random.randint(1, 9)

operatorMin1 = random.randint(1, 4)

op12Min, operatorCharMin = firstOperator(Min_1, Min_2, operatorMin1)

Min_3 = minutes - op12Min
Min_3 = round(Min_3, 2)

operatorChar2Min="+"

if Min_3<0:
    operatorChar2Min = ""


while True:

# Clear Screen
 turtle.clear()

 # Set values for SECOND
 # Process is the same as HOUR and MINUTE
 Sec_1 = random.randint(1, 9)
 Sec_2 = random.randint(1, 9)

 operatorSec1 = random.randint(1, 4)

 op12Sec, operatorCharSec = firstOperator(Sec_1, Sec_2, operatorSec1)

 Sec_3 = seconds - op12Sec
 Sec_3=round(Sec_3 , 2)

 operatorChar2Sec = "+"

 if Sec_3 < 0:
  operatorChar2Sec = ""

# Write HOUR, MINUTE and SECOND to the screen
 turtle.write(str(Hr_1).zfill(2)+ operatorCharHr + str(Hr_2).zfill(2) + operatorChar2Hr + str(Hr_3).zfill(2)+ "   HR\n"
        + str(Min_1).zfill(2)+ operatorCharMin + str(Min_2).zfill(2) + operatorChar2Min + str(Min_3).zfill(2) + "   MIN\n"
        + str(Sec_1).zfill(2)+ operatorCharSec + str(Sec_2).zfill(2) + operatorChar2Sec + str(Sec_3).zfill(2)+"   SEC\n"
        ,move=False, align="center",font=("DS-Digital",65,"bold"))

 # Set value for second when second<60
 seconds = seconds + 1

 # Wait for 1 seconds
 time.sleep (1)

# Set Second and Minute when Second = 60!
 if seconds == 60:
  seconds = 0
  minutes = minutes + 1

# Set Screen for MINUTE
  Min_1 = random.randint(1, 9)
  Min_2 = random.randint(1, 9)

  operatorMin1 = random.randint(1, 4)

  op12Min, operatorCharMin = firstOperator(Min_1, Min_2, operatorMin1)

  Min_3 = minutes - op12Min
  Min_3 = round(Min_3, 2)

 operatorChar2Min = "+"

 if Min_3 < 0:
     operatorChar2Min = ""

# Set Minute and Hour when Minute = 60!
 if minutes == 60:
  minutes = 0
  hours = hours + 1

# Set Screen for HOUR
  Hr_1 = random.randint(1, 9)
  Hr_2 = random.randint(1, 9)

  operatorHr1 = random.randint(1, 4)

  op12Hr, operatorCharHr = firstOperator(Hr_1, Hr_2, operatorHr1)

  Hr_3 = hours - op12Hr
  Hr_3 = round(Hr_3, 2)

  operatorChar2Hr = "+"

  if Hr_3 < 0:
      operatorChar2Hr = ""