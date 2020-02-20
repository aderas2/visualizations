#!/usr/bin/env python
# coding: utf-8

# In[21]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[22]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[29]:


tips = pd.read_csv('tips.csv')


# In[30]:


tips.head()


# In[32]:


sns.distplot(tips['tal_bill'], kde=True)


# In[33]:


sns.distplot(tips['tal_bill'], kde=False)


# In[39]:


sns.distplot(tips['tal_bill'],kde=False, bins=100)


# In[35]:


sns.jointplot(x='tal_bill',y='tip',data=tips) #scatter plots btw distplots


# In[36]:


sns.jointplot(x='tal_bill',y='tip',data=tips,kind='hex') #scatter plots btw hexagon plots


# In[37]:


sns.jointplot(x='tal_bill',y='tip',data=tips,kind='reg') #scatter plots btw regression plots


# In[40]:


sns.jointplot(x='tal_bill',y='tip',data=tips,kind='kde') #scatter plots btw kde plots


# In[41]:


sns.pairplot(tips)


# In[42]:


sns.pairplot(tips, hue='sex')


# In[43]:


sns.rugplot(tips['tal_bill'] )


# In[44]:


sns.kdeplot(tips['tal_bill'])


# In[45]:


sns.barplot(x='sex',y='tal_bill',data=tips)


# In[46]:


sns.barplot(x='sex',y='tal_bill',data=tips,estimator=np.std)


# In[47]:


sns.countplot(x='sex',data=tips)


# In[48]:


sns.boxplot(x='day',y='tal_bill',data=tips)


# In[49]:


sns.boxplot(x='day',y='tal_bill',data=tips,hue='smoker')


# In[54]:


sns.violinplot(x='day',y='tal_bill',data=tips)


# In[52]:


sns.violinplot(x='day',y='tal_bill',data=tips,hue='sex')


# In[55]:


sns.violinplot(x='day',y='tal_bill',data=tips,hue='sex', split=True)


# In[56]:


sns.stripplot(x='day',y='tal_bill',data=tips)


# In[57]:


sns.stripplot(x='day',y='tal_bill',data=tips,jitter=False)


# In[59]:


sns.stripplot(x='day',y='tal_bill',data=tips,hue='sex',split=True)


# In[60]:


sns.stripplot(x='day',y='tal_bill',data=tips,hue='sex',dodge=True)


# In[71]:


sns.swarmplot(x='day',y='tal_bill',data=tips)


# In[69]:


sns.violinplot(x='day',y='tal_bill',data=tips)
sns.swarmplot(x='day',y='tal_bill',data=tips,color='black')


# In[72]:


sns.factorplot(x='day',y='tal_bill',data=tips,kind='bar')


# In[73]:


sns.factorplot(x='day',y='tal_bill',data=tips,kind='violin')


# In[76]:


sns.factorplot(x='day',y='tal_bill',data=tips,kind='strip')


# # Matric plots (Heat Maps)

# In[77]:


tips.head()


# In[79]:


flights = pd.read_csv('flight.csv')


# In[80]:


flights.head()


# In[82]:


tc=tips.corr()


# In[83]:


tc


# In[84]:


sns.heatmap(tc)


# In[85]:


sns.heatmap(tc,annot=True)


# In[86]:


sns.heatmap(tc,annot=True,cmap='coolwarm')


# In[87]:


flights


# In[89]:


flights.pivot_table(index='month',columns='year',values='passengers')


# In[90]:


fp = flights.pivot_table(index='month',columns='year',values='passengers')


# In[91]:


fp


# In[92]:


sns.heatmap(fp)


# In[94]:


sns.clustermap(fp,cmap='coolwarm') 


# In[95]:


sns.clustermap(fp,cmap='coolwarm',standard_scale=1)  #using standard scale of 1


# In[96]:


iris=pd.read_csv('iris.csv')


# In[97]:


iris


# In[98]:


sns.pairplot(iris)


# In[100]:


sns.PairGrid(iris)


# In[101]:


pg=sns.PairGrid(iris)


# In[110]:


pg=sns.PairGrid(iris)
pg.map_diag(sns.distplot)
pg.map_upper(sns.scatterplot)
pg.map_lower(sns.kdeplot)


# In[113]:


tips


# In[114]:


fg=sns.FacetGrid(data=tips,col='time',row='smoker')


# In[115]:


fg=sns.FacetGrid(data=tips,col='time',row='smoker')
fg.map(sns.distplot,'tal_bill')


# In[116]:


fg.savefig('distplot.pdf')


# In[117]:


fg=sns.FacetGrid(data=tips,col='time',row='smoker')
fg.map(sns.scatterplot,'tal_bill','tip')


# # Regression plot

# In[118]:


tips


# In[119]:


sns.lmplot(x='tal_bill',y='tip',data=tips)


# In[120]:


sns.lmplot(x='tal_bill',y='tip',data=tips,hue='sex') 


# In[121]:


sns.lmplot(x='tal_bill',y='tip',data=tips,hue='sex',markers=['o','v']) 


# In[125]:


sns.lmplot(x='tal_bill',y='tip',data=tips,col='sex',row='time')


# In[126]:


sns.lmplot(x='tal_bill',y='tip',data=tips,col='day',row='time',hue='sex')


# In[127]:


sns.lmplot(x='tal_bill',y='tip',data=tips,col='day',hue='sex')


# In[128]:


sns.lmplot(x='tal_bill',y='tip',data=tips,col='day',hue='sex',aspect=0.6,size=8)


# # Style and Colour

# In[129]:


tips


# In[130]:


sns.countplot(x='sex',data=tips)


# In[131]:


sns.set_style('white')
sns.countplot(x='sex',data=tips)


# In[132]:


sns.set_style('ticks')
sns.countplot(x='sex',data=tips)


# In[133]:


sns.set_style('darkgrid')
sns.countplot(x='sex',data=tips)


# In[134]:


sns.set_style('whitegrid')
sns.countplot(x='sex',data=tips)


# In[138]:


sns.set_style('ticks')
sns.countplot(x='sex',data=tips)
sns.despine()


# In[139]:


plt.figure(figsize=(12,3))
sns.countplot(x='sex',data=tips)


# In[141]:


sns.set_context('poster')
sns.countplot(x='sex',data=tips)


# In[143]:


sns.set_context('notebook')
sns.countplot(x='sex',data=tips)


# In[ ]:




