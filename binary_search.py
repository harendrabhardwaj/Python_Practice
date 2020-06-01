# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 17:56:19 2019

@author: user
"""

def Binary_Search(item, max, min, tar):
    mid =(max+min)//2
    if(min>max):
        print("element not found")
    elif (tar>item[mid]):
        min=mid+1
        Binary_Search(item, max, min, tar)
    elif (tar<item[mid]):
        max=mid-1
        Binary_Search(item, max, min, tar)
    else:
       print("Target element is at index {}"  .format(item[mid]))


item = [1,2,3,4,5,6,7,8,9,11]
tar=8
max = len(item)-1
min = 0
Binary_Search(item, max, min, tar)
 
