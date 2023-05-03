#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *


# In[2]:


window = Tk()


# In[3]:


window.title("Welcome To Shangui University")


# In[4]:


window.minsize(width = 200, height = 400)


# In[5]:


window.maxsize(width = 400, height = 800)


# In[6]:


f1 = Frame()


# In[7]:


f1.pack()


# In[8]:


f2 = Frame()


# In[9]:


f2.pack(side = BOTTOM)


# In[11]:


l1 = Label(f1, text = "Great Learning")


# In[12]:


l1.pack()


# In[13]:


l2 = Label(f2, text = "bottom")


# In[14]:


l2.pack()


# In[15]:


window.mainloop()


# In[ ]:




