# -*- coding: utf-8 -*-
"""
Python Proficiency Demo Assignment
"""

class module_one:
    def __init__(self, x):  # init method or constructor
        self.lst = list(range(0,x+1))
       
    def sub_list_sliced(self,y):
        if(y > len(self.lst) or (y <= 0)):
            return ("The sliced sublist's size is smaller than zero; size of the original list is greater")
       
        else:
            sliced_sublist = self.lst[:y]
            return sliced_sublist
            