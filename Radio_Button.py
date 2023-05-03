#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *


# In[2]:


window = Tk()


# In[3]:


window.title("Welcome To great Learning")


# In[4]:


window.minsize(width = 200, height = 400)


# In[5]:


window.maxsize(width = 400, height = 800)


# In[6]:


v = IntVar()


# In[8]:


def edtech():
    print(v.get())


# In[9]:


rb1 = Radiobutton(window, text = "Yes", value = 1, variable = v)


# In[10]:


rb1.pack()


# In[11]:


rb2 = Radiobutton(window, text = "No", value = 0, variable = v)


# In[12]:


rb2.pack()


# In[13]:


b1 = Button(window, text = "Enter", command = edtech)


# In[14]:


b1.pack()


# In[16]:


window.mainloop()


# In[ ]:




