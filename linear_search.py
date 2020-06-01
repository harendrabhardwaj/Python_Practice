# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 17:45:45 2019

@author: user
"""

items = [10, 20, 30, 40, 50, 60]
i=flag=0
print("Items are",items)
x = int(input("Enter item to be Search:"))
while i < len(items):
        if items[i]==x:
            flag=1
            break
        i=i+1
if flag==1:
    print("Found at",i+1)
else:
    print("Not Found")