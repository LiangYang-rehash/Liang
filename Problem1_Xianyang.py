# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 04:36:12 2020

@author: Administrator
"""

a=eval(input('How much is your original bill? '))
b=eval(input('What percentage is your tip? '))

c=a*(b/100)
d=a+c

print('Your tip based on',b,'% is',c)
print('Your total bill is',d)


