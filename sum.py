# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 16:27:30 2020

@author: user
"""
sum=0
prod=1
ran = int(input())
choice = int(input())
if choice == 1:
    for i in range(1,ran+1):
        sum=sum+i
    print(sum)
elif choice == 2:
    for i in range(1,ran+1):
        prod=prod*i
    print(prod)
else:
    print("-1")