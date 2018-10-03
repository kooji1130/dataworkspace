#!/usr/bin/env python
# coding: utf-8

# In[12]:


fruit=['apple','banana','cherry','coconut','grape','guava','melon','lemon','orange','kiwi']
print('(1)')
print(fruit)
print('(2)')
print(fruit[4])
print('(3)')
print(fruit[-1])
print('(4)')
print(fruit[2:6])
print('(5)')
pickfruit=fruit.pop(2)
print(pickfruit)
print(fruit)
print('(6)')
fruit.insert(1,'蜜桃')
print(fruit)
print('(7)')
fruit.extend(['非洲甜橙'])
print(fruit)
print('(8)')
country=['亞洲','非洲','美洲']
print(country)
print('(9)')
fruit=fruit+country
print(fruit)

