#!/usr/bin/env python
# coding: utf-8

# In[15]:


from tkinter import *


# In[16]:


window = Tk()


# In[17]:


window.title("Welcome To Great Learning")


# In[18]:


window.minsize(width = 200, height = 400)


# In[19]:


window.maxsize(width = 400, height = 800)


# In[6]:


lb = Listbox(window, width = 20)


# In[7]:


lb.pack()


# In[8]:


l1 = ["Sardar", "Ali khan", "Magsi", "Sahb"]


# In[9]:


for i in l1:
    lb.insert(END, i)


# In[10]:


def edtech():
    lb.delete(ANCHOR)


# In[11]:


b1 = Button(window, text = "Remove", bg = "Red", command = edtech)


# In[12]:


b1.pack()


# In[13]:


window.mainloop()


# In[ ]:




