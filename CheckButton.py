#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *


# In[2]:


window = Tk()


# In[3]:


window.title("Online Web based Form")


# In[4]:


window.minsize(width = 200, height = 400)


# In[5]:


window.maxsize(width = 400, height = 800)


# In[7]:


cb = Checkbutton(window, text = "Male")


# In[8]:


cb.pack()


# In[9]:


window.mainloop()


# In[ ]:




