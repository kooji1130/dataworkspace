#!/usr/bin/env python
# coding: utf-8

# In[19]:


memberlist=[('林姍',155,45),
            ('王志祥',175,85),
            ('李明立',172,68),
            ('黃婷婷',162,52),
            ('張文智',180,72),
            ('陳怡君',158,48),
            ('王凱群',170,80),
            ('林曉曉',156,70)]
List=[]
print("="*30)
print("以下同學體重過重，請平日進行飲食的調整，以維持健康的身體")
print("姓名   BMI")
for data in memberlist:
    templ=float((data[1]/100)**2)
    tempw=int(data[2])
    tempbmi=tempw/templ
    tempbmi = round(tempbmi,10)
    if tempbmi>=27:
        print(data[0],tempbmi)
------------------------------------------------------------------------------------------------
name=['林姍','王志祥','李明立','黃婷婷','張文智','陳怡君','王凱群','林曉曉']
height=[155,175,172,162,180,158,170,156]
weight=[45,85,68,52,72,48,80,70]
student=[]

for i in range (len(name)):
  student.append([])
  student[i].append(name[i])
  student[i].append(height[i])
  student[i].append(weight[i])        
print(student)

List=[]
print("="*30)
print("以下同學體重過重，請平日進行飲食的調整，以維持健康的身體")
print("姓名   BMI")
for data in student:
    templ=float((data[1]/100)**2)
    tempw=int(data[2])
    tempbmi=tempw/templ
    tempbmi = round(tempbmi,10)
    if tempbmi>=27:
        print(data[0],tempbmi)
    


