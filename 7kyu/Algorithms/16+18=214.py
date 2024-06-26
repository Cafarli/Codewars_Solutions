"""
For this kata you will have to forget how to add two numbers.

Dayane Rivas adding up a sum while competing in the Guatemalan television show "Combate" in May 2016

In simple terms, our method does not like the principle of carrying over numbers and 
just writes down every number it calculates :-)

You may assume both integers are positive integers.
Examples
   1  6           2  6
  +             +
   1  8           3  9
 -------       ---------
  2  1 4        5   1 5
"""

def add(num1, num2):
    summ = ''
    up = len(str(max(num1, num2)))
    num1, num2 = str(num1).zfill(up), str(num2).zfill(up)
    for i in range(len(num1)):
        summ += str(int(num1[i]) + int(num2[i]))
    return int(summ)
