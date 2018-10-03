#!/usr/bin/env python
# coding: utf-8

# In[17]:


people=[('林威豪','台北市'),
        ('黃安安','高雄市'),
        ('林湘琦','台中市'),
        ('陳遠見','台南市'),
        ('林萊萱','台中市'),
        ('許志祥','台北市'),
        ('呂姍姍','嘉義市'),
        ('張柏凱','桃園市')]
pick=[]
for member in people: 
    if member[1]=='台北市':
        temp=people.pop(people.index(member))
        pick.append(temp)
        print(member[1])
print(pick)
print(people)

