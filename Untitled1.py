#!/usr/bin/env python
# coding: utf-8

# In[1]:


d1={123:"vis"}


# In[2]:


d1


# In[3]:


d1[123]


# In[4]:


d2={123:"vis"}


# In[5]:


d2


# In[6]:


d1+d2


# In[7]:


C


# In[8]:


d3={"laptop":hp : "laptop":dell}


# In[9]:


d3={"laptop":hp,"laptop":dell}


# In[14]:


d3={"laptop":'hp',"laptop":'dell'} d3


# In[15]:


d3


# In[1]:


d={"vishal":100, "komal":99 }


# In[2]:


d.pop("komal")


# In[3]:


d


# In[4]:


if marks>=80:


# In[5]:


if marks>=80:
    print("you will be a part A0 batch ")


# In[6]:


if marks>=80:


# In[8]:


marks=80
   if marks >=80:
       print("you will be a part A0 batch ")
       elif marks >=60 and marks <80:
           print("you will be part A1 batch")
           elif marks >=40 and marks <60:
               else marks>=40
               print("you will be part of A3")


# In[9]:


marks=80
    if marks >=80:
        print("you will be a part A0 batch ")
        elif marks >=60 and marks <80:
            print("you will be part A1 batch")
            elif marks >=40 and marks <60:
                else marks>=40
                print("you will be part of A3")


# In[10]:


marks=100
    if marks >=80:
        print("you will be a part A0 batch ")
        elif marks >=60 and marks <80:
            print("you will be part A1 batch")
            elif marks >=40 and marks <60:
                else 
                print("you will be part of A3")


# In[11]:


marks=100
    if marks >=80 :
        print("you will be a part A0 batch ")
        elif marks >=60 and marks <80:
            print("you will be part A1 batch")
            elif marks >=40 and marks <60:
                else :
                print("you will be part of A3")


# In[13]:


marks = 100
    if marks >=80 :
        print("you will be a part A0 batch ")
        elif marks >=60 and marks <80:
            print("you will be part A1 batch")
            elif marks >=40 and marks <60:
                else :
                print("you will be part of A3")


# In[14]:


marks = 100
    if marks >=80 :
        print("you will be a part A0 batch ")
        elif marks >=60 and marks <80:
            print("you will be part A1 batch")
            elif marks >=40 and marks <60:
                else :
                print("you will be part of A3")
                


# In[15]:


marks = 100
if marks >= 80:
    print("You will be a part of A0 batch")
elif marks >= 60 and marks < 80:
    print("You will be a part of A1 batch")
elif marks >= 40 and marks < 60:
    print("You will be a part of A2 batch")
else:
    print("You will be a part of A3 batch")

T


# In[16]:


marks = 100
if marks >= 80:
    print("You will be a part of A0 batch")
elif marks >= 60 and marks < 80:
    print("You will be a part of A1 batch")
elif marks >= 40 and marks < 60:
    print("You will be a part of A2 batch")
else:
    print("You will be a part of A3 batch")
    


# In[17]:


price =int(input("User input"))
if price > 1000 :
  print ("I will purcase ")
elif price < 1000 :
  print("i will not purcase ")


# In[18]:


price =int(input("User input"))
if price < 1000 :
  print ("I will purcase ")
elif price >1000 :
  print("i will not purcase ")


# In[19]:


l=[1,2,3,4,5]


# In[20]:


l


# In[21]:


l[0]+1


# In[22]:


l


# In[23]:


l=l[0]+1


# In[24]:


l


# In[25]:


l1=[]


# In[26]:


l


# In[27]:


l1


# In[28]:





# In[29]:


l1


# In[30]:


l=[1,2,3,4,5]
l1=[]
for i in  l :
   print (i+1)
l1.append(i+1)


# In[31]:


l=[1,2,3,4,5]
l1=[]
for i in  l :
   print (i+1)
l1.append(i+1)
l1


# In[32]:





# In[33]:


l


# In[34]:


l1


# In[35]:


l1=[]
for i in  l :
   print (l)
l1.append(i+1)
l1


# In[47]:


l=[1,2,3,3,4,5]
l1= []
for i in  l :
 print(i+1)
l1.append(i+1)
l1


# In[48]:





# In[50]:


l=["vis","div","sis"]
l1=[]
for i in l :
    print(i)
    l1.append((i.upper())


# In[57]:



   


# In[52]:


l1


# In[58]:


l=["vis","div","sis"]
l1=[]
for i in l :
    print(i)
    l1.append(i.upper())


# In[59]:


l1


# In[60]:


l=[1,2,3,4,"vis",500,600,"doc"]


# In[61]:


l


# In[62]:


l2=[]


# In[64]:


l1=[]


# ## 

# In[65]:


l2


# In[66]:


l


# In[67]:


l1_num =[]


# In[69]:


l2_str =[]


# In[77]:


for i in l :
 if type(i) == int or type(i) == float :
        l1_num.append(i)
else :
    l2_str.append(i)


# In[78]:


l = [1, 2, 3, 4, 'vis', 500, 600, 'doc']
l1_num = []
l2_str = []

for i in l:
    if type(i) == int or type(i) == float:
        l1_num.append(i)
    else:
        l2_str.append(i)
        


# In[80]:


l = [1, 2, 3, 4, 'vis', 500, 600, 'doc']
l1_num = []
l2_str = []

for i in l:
    if type(i) == int or type(i) == float:
        l1_num.append(i)
    else:
        l2_str.append(i)


# In[81]:


l1_num


# In[82]:


l2_str


# In[83]:


l = [1, 2, 3, 4, 'vis', 500, 600, 'doc']
l1_num = []
l2_str = []

for i in l:
    if type(i) == int or type(i) == float:
        l1_num.append(i)
    else:
        l2_str.append(i)

print(l1_num)
print(l2_str)


# In[ ]:




