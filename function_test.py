#!/usr/bin/env python
# coding: utf-8

# In[42]:


# Method1: import factorial
from math import factorial as fact

ans = 0
for n in range (1,11): #range 1:10
    left = fact(n) # left = n!
    right = fact(n+1) #right = (n+1)!
    value = left * right # value = n! * (n+1)!
    ans += value # sum up all value from 1 to 10
print (ans) # ans = 146181741036638

# Method2: without importing factorial

def fact(num): #計算階層
    i = 1
    while (num >= 1):
        i *= num # num * (num-1) * (num-1-1) *...
        num -= 1 #遞減1
    return (i)

#代入公式
ans = 0
for n in range (1,11): #range 1:10
    left = fact(n) # left = n!
    right = fact(n+1) #right = (n+1)!
    value = left * right # value = n! * (n+1)!
    ans += value # sum up all value from 1 to 10
print (ans) # ans = 146181741036638


# In[ ]:





# In[ ]:





# In[ ]:




