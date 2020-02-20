#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pandas as pd


# In[36]:


import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# In[37]:


from plotly import __version__


# In[38]:


print(__version__)


# In[39]:


import cufflinks as cf


# In[40]:


from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot


# In[41]:


init_notebook_mode(connected=True)


# In[ ]:





# In[42]:


cf.go_offline()


# In[43]:


#data
df = pd.DataFrame(np.random.randn(100,4),columns='A B C D'.split())


# In[44]:


df.head()


# In[45]:


df2 = pd.DataFrame({'Category':['A','B','C'],'Values':[32,43,50]})


# In[46]:


df2


# In[47]:


df.plot()


# In[48]:


df.iplot()


# In[49]:


df.iplot(kind='scatter',x='A',y='B')


# In[54]:


df.iplot(kind='scatter',x='A',y='B',mode='markers',size=20)


# In[56]:


df2.iplot(kind='bar',x='Category',y='Values')


# In[57]:


df.iplot(kind='bar')


# In[61]:


df.mean().iplot(kind='bar')


# In[65]:


df.sum().iplot(kind='bar')


# In[66]:


df.iplot(kind='box')


# In[67]:


df3=pd.DataFrame({'x':[2,3,4,5,6],'y':[30,43,56,76,87],'z':[9,3,5,6,1]})


# In[68]:


df3


# In[70]:


df3.iplot(kind='surface',color='ylburd')


# In[71]:


df['A'].iplot(kind='hist',bins=50)


# In[72]:


df.iplot(kind='hist')


# In[77]:


df[['A','B']]


# In[78]:


df[['A','B']].iplot(kind='spread')


# In[80]:


df.iplot(kind='bubble',x='A',y='B',size='C',color='orange')


# In[81]:


df.scatter_matrix()


# In[ ]:




