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
    

