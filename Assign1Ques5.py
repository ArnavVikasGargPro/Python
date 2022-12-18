#Write a program that prints out the sine and cosine of the angles ranging 
#from 0 to 345◦ in 15◦ increments. Each result should be rounded to 4 
#decimal places.
# Sine Series-----
import math 
print("Sine series is as shown below\n") 
for i in range(0,360,15):
     angle=math.radians(i) 
     value=math.sin(angle)
     rounded= round(value,4)

     print("sine",i,":", rounded)
    
print("Finished printing the sine series for a given range")
# Cosine series ---------

import math 
print("Cosine  series is as shown below\n") 
for i in range(0,360,15):
     angle=math.radians(i) 
     value=math.cos(angle)
     rounded= round(value,4)

     print("cosine",i,":", rounded)
    
print("Finished printing the cosine series for a given range")

#Ece 22105015
