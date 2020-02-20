#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import pandas as pd


# In[7]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[8]:


df1 = pd.read_csv('df1',index_col=0)


# In[9]:


df1.head()


# In[10]:


df1


# In[11]:


df2 = pd.read_csv('df2')


# In[12]:


df2.head()


# In[17]:


df1['A'].hist(bins=30)


# In[19]:


df1['A'].plot()


# In[20]:


df1['A'].plot(kind='hist')


# In[27]:


df1['A'].plot(kind='kde')


# In[28]:


df2.plot.area()


# In[30]:


df2.plot.area(alpha=0.4)


# In[31]:


df2.plot.bar()


# In[32]:


df2.plot.bar(stacked=True)


# In[35]:


df1.plot.hist(bins=50)


# In[39]:


df1.plot.line(y='B')


# In[42]:


df1.plot.line(y='B',figsize=(15,3))


# In[43]:


df1.plot.scatter('A',y='B')


# In[45]:


df1.plot.scatter('A',y='B',c='C',cmap='coolwarm')


# In[47]:


df1.plot.scatter('A',y='B',s=df1['C']*100)


# In[48]:


df2.plot.box()


# In[51]:


df=pd.DataFrame(np.random.randn(1000,2),columns=['a','b'])


# In[53]:


df.head()


# In[56]:


df.plot.hexbin(x='a',y='b',gridsize=25,cmap='coolwarm')


# In[61]:


df2.plot.kde()


# In[62]:


df.plot()


# In[63]:


df3 = pd.read_csv('df3')


# In[64]:


df3.info()


# In[65]:


df3.head()


# In[69]:


df3.plot.scatter(x='a',y='b',figsize=(12,2))


# In[71]:


df3['a'].plot.hist()


# In[73]:


df3['a'].plot.hist(bins=50,color='red')


# In[74]:


df3.plot.box()


# In[87]:


df3[['a','b']].plot.box()


# In[79]:


df3['d'].plot.kde()


# In[85]:


df3['d'].plot.kde(linestyle='--',color='red',linewidth=5)


# In[86]:


df3.plot.area()


# In[88]:


df3.ix[0:30].plot.area()


# In[90]:


import matplotlib.pyplot as plt
df3.ix[0:30].plot.area()
plt.legend(loc='center left',bbox_to_achor=(1.0,.5))


# In[ ]:




