# -*- coding: utf-8 -*-
"""3rdClassAssignment.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-7y4UgX8QtW-SEdT3b1Tlqxa3OoWRdJ0

Assignment1: Write a python program to print all number in a range divisble by a given number
"""

num = int(input("Enter a number between 50 to 150 = "))
print("Numbers divisible by",num,"are = ")
for i in range(50,150):
  if i%num==0:
    print(i)