#!/usr/bin/env python
# coding: utf-8

# In[1]:


import snap
import random
import numpy as np
import pandas as pd
import networkx as nx


# In[3]:


Rnd = snap.TRnd()
Graph = snap.GenRMat(80, 50, .5, .15, .1, Rnd)
src=[]
dest=[]
for EI in Graph.Edges():
    src.append(EI.GetSrcNId())
    dest.append(EI.GetDstNId())
    print("Edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))


# In[4]:


time = [random.randrange(0, 50) for i in range(50)]
df = pd.DataFrame(list(zip(src,dest,time)), columns=['i','j','t'])


# In[5]:


N = nx.from_pandas_edgelist(df,source='i',target='j',edge_attr='t',create_using=nx.DiGraph())
print(N.number_of_nodes())
print(N.number_of_edges())


# In[ ]:




