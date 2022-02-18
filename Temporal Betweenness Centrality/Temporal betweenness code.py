#!/usr/bin/env python
# coding: utf-8
import numpy as np
import pandas as pd
import networkx as nx
import csv
import sys
import teneto
import os


#https://teneto.readthedocs.io/en/latest/api/teneto.networkmeasures.temporal_betweenness_centrality.html#teneto.networkmeasures.temporal_betweenness_centrality
def outputTBWC(graphPath):
    df = pd.read_csv(graphPath, usecols=['i', 'j', 't'])
    graph= teneto.TemporalNetwork(from_df=df,nettype='bd')
    print(graph)
    bwc = teneto.networkmeasures.temporal_betweenness_centrality(tnet = graph, calc='overtime')
    print(bwc)



directory = '/home/bhagat_aryaman/Modified-PageRank/smallSampleGraph/pythonDatasets'

 
# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        outputTBWC(f)


    