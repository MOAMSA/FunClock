import datetime
import random

# Set current time
now=str(datetime.datetime.now())
seconds=now[17:19]
minutes=now[14:16]
hours=now[11:13]
seconds=int(seconds)
minutes=int(minutes)
hours=int(hours)


def whichSign(Val1,Val2,Sign):
 if Sign == 1:
     Val12 = Val1 + Val2
     SignChar="+"
 elif Sign == 2:
     Val12 = Val1 - Val2
     SignChar = "-"
 elif Sign == 3:
     Val12 = Val1 * Val2
     SignChar = "*"
 elif Sign == 4:
     Val12 = Val1 / Val2
     SignChar = "/"


 return  Val12, SignChar



import time
from turtle import *

t1=Turtle(visible=False)
t1.screen.title("CLOCK!")
t1.screen.screensize()
t1.pencolor("red")
t1.screen.bgcolor("#000000")
Hr_1 = random.randint(1, 9)
Hr_2 = random.randint(1, 9)
SignHr1 = random.randint(1, 4)
Val12Hr, SignCharHr = whichSign(Hr_1, Hr_2, SignHr1)
Hr_3 = hours - Val12Hr
Hr_3 = round(Hr_3, 2)

SignChar2Hr="+"
if Hr_3 < 0:
 SignChar2Hr = ""


Min_1 = random.randint(1, 9)
Min_2 = random.randint(1, 9)
SignMin1 = random.randint(1, 4)
Val12Min, SignCharMin = whichSign(Min_1, Min_2, SignMin1)
Min_3 = minutes - Val12Min
Min_3 = round(Min_3, 2)

SignChar2Min="+"
if Min_3<0:
    SignChar2Min = ""

while True:
 t1.clear()



 Sec_1 = random.randint(1, 9)
 Sec_2 = random.randint(1, 9)
 SignSec1 = random.randint(1, 3)
 Val12Sec, SignCharSec = whichSign(Sec_1, Sec_2, SignSec1)
 Sec_3 = seconds - Val12Sec
 Sec_3=round(Sec_3 , 2)

 SignChar2Sec = "+"
 if Sec_3 < 0:
  SignChar2Sec = ""

 t1.write(str(Hr_1).zfill(2)+ SignCharHr + str(Hr_2).zfill(2) + SignChar2Hr + str(Hr_3).zfill(2)+ "   HR\n"
        + str(Min_1).zfill(2)+ SignCharMin + str(Min_2).zfill(2) + SignChar2Min + str(Min_3).zfill(2) + "   MIN\n"
        + str(Sec_1).zfill(2)+ SignCharSec + str(Sec_2).zfill(2) + SignChar2Sec + str(Sec_3).zfill(2)+"   SEC\n"
        ,move=False, align="center",font=("DS-Digital",65,"bold"))



 seconds = seconds + 1
 time.sleep (1)
 if seconds == 60:
  seconds = 0
  minutes = minutes + 1

  Min_1 = random.randint(1, 9)
  Min_2 = random.randint(1, 9)
  SignMin1 = random.randint(1, 4)
  Val12Min, SignCharMin = whichSign(Min_1, Min_2, SignMin1)
  Min_3 = minutes - Val12Min
  Min_3 = round(Min_3, 2)

 SignChar2Min = "+"
 if Min_3 < 0:
     SignChar2Min = ""

 if minutes == 60:
  minutes = 0
  hours = hours + 1

  Hr_1 = random.randint(1, 9)
  Hr_2 = random.randint(1, 9)
  SignHr1 = random.randint(1, 4)
  Val12Hr, SignCharHr = whichSign(Hr_1, Hr_2, SignHr1)
  Hr_3 = hours - Val12Hr
  Hr_3 = round(Hr_3, 2)

  SignChar2Hr = "+"
  if Hr_3 < 0:
      SignChar2Hr = ""