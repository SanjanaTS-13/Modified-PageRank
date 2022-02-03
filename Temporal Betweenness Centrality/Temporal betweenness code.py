#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import networkx as nx


# In[3]:


#Ignore the warning
import teneto


# In[4]:


#Generate a dataframe for the graph or use any graph generators and convert to dataframe
np.random.seed(1245)
df = pd.DataFrame(np.random.randint(0,56,size=(56, 3)), columns=['i','j','t'])


# In[9]:


graph= teneto.TemporalNetwork(from_df=df,nettype='bd')


# In[ ]:


bwc = teneto.networkmeasures.temporal_betweenness_centrality(tnet = graph, calc='overtime')
bwc


# In[11]:


#https://teneto.readthedocs.io/en/latest/api/teneto.networkmeasures.temporal_betweenness_centrality.html#teneto.networkmeasures.temporal_betweenness_centrality

