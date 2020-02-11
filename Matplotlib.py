#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt


# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


import numpy as np


# In[6]:


x=np.linspace(0,5,11)
y=x**2


# In[7]:


x


# In[8]:


y


# In[13]:


plt.plot(x,y)
plt.xlabel('X label')
plt.ylabel('Y label')
plt.title('Title')


# In[11]:


import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()


# In[16]:


plt.subplot(1,2,1)
plt.plot(x,y,'r')

plt.subplot(1,2,2)
plt.plot(y,x,'b')


# In[17]:


#object orientation


# In[24]:


fig = plt.figure()
axes=fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y)
axes.set_xlabel('X label')
axes.set_ylabel('Y label')
axes.set_title('Set Title')


# In[31]:


fig = plt.figure()
axes1=fig.add_axes([0.1,0.1,0.8,0.8])
axes2=fig.add_axes([0.2,0.5,0.4,0.3])
axes1.plot(x,y)
axes1.set_title('LARGER PLOT')
axes2.plot(y,x)
axes2.set_title('SMALLER PLOT')


# In[34]:


fig,axes=plt.subplots(nrows=3,ncols=3)
#axes.plot(x,y)
plt.tight_layout()


# In[36]:


fig,axes=plt.subplots(nrows=1,ncols=2)

for current_ax in axes:
    current_ax.plot(x,y)
#axes.plot(x,y)


# In[37]:


axes


# In[42]:


fig,axes=plt.subplots(nrows=1,ncols=2)
axes[0].plot(x,y)
axes[0].set_title('First Plot')

axes[1].plot(y,x)
axes[1].set_title('Second Plot')


# # FigureSize and DPI

# In[46]:


fig= plt.figure(figsize=(3,2))
ax= fig.add_axes([0,0,1,1])
ax.plot(x,y)


# In[50]:


fig= plt.figure(figsize=(8,2))
ax= fig.add_axes([0,0,1,1])
ax.plot(x,y)


# In[56]:


fig,axes= plt.subplots(nrows=2,ncols=1,figsize=(8,2))
axes[0].plot(x,y)
axes[1].plot(y,x)
plt.tight_layout()


# In[59]:


fig.savefig('my_first_save.jpg',dpi=500)


# In[73]:


fig=plt.figure()
ax1= fig.add_axes([0,0,1,1])
ax1.plot(x,x**2,label='X Squared')
ax1.plot(x,x**3,label='X Cubed')
ax1.legend(loc=(0.1,0.2))


# In[111]:


fig.savefig('ax_plot.png',dpi=1000)


# # plot Appearance

# In[108]:


fig=plt.figure()
ax = fig.add_axes([0,0,1,1])
#ax.plot(x,y,color='green')
ax.plot(x,y,color='#ff8c00',linewidth=.5,linestyle='-',marker='o',markersize=20,markerfacecolor='yellow',
       markeredgewidth=3,markeredgecolor='blue')


# In[109]:


plt.scatter(x,y)


# In[112]:


plt.savefig('testing_plt.pdf')


# In[115]:


import numpy as np
6/2(2+1)


# In[ ]:




