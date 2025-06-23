'''
Asterisks
We can render an ASCII art pyramid with N levels by printing N rows of asterisks, where the top row has a single asterisk in the center and each successive row has two additional asterisks on either side.

Here's what that looks like when N is equal to 3.
  *  
 *** 
*****

And here's what it looks like when N is equal to 5.
    *    
   ***   
  ***** 
 ******* 
********* 

Can you write a program that generates this pyramid with a N value of 10?
[execution time limit] 4 seconds (py)
[memory limit] 2g
'''
# import requests
# import mysql.connector
# import pandas as pd
asteriskAddition = 0
lenOfPyramid = 10
spaceToOffset = lenOfPyramid-1
for i in range(1,lenOfPyramid+1):
  print( ' '*spaceToOffset + '*'*(i+asteriskAddition) )
  asteriskAddition = asteriskAddition+1
  spaceToOffset = spaceToOffset-1
