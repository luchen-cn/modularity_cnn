import keras
from keras.models import load_model
import os
import sys
import numpy as np

import networkx as nx
from cdlib import algorithms
import community

def calc(a_file):

    res = 1.0
    model_a = load_model(a_file)

    lim_node = 0

    prefix_from=0
    prefix_to=0
    edges = []

    for env_l, layer in enumerate(model_a.layers):

        weights = layer.get_weights()
        if len(weights) == 2:
            weights_shape = weights[0].shape
            if len(weights_shape) == 4:
                prefix_to = prefix_from + weights_shape[2]
                k_var = []
                k_var_id = []
                edges_tmp = {}
                for i4 in range(weights_shape[3]):
                    for i3 in range(weights_shape[2]):
                        w_kernel = []
                        for i2 in range(weights_shape[1]):
                            for i1 in range(weights_shape[0]):
                                w_val = weights[0][i1][i2][i3][i4]
                                w_kernel.append(w_val)
                        k_var = np.var(np.array(w_kernel))
                        edges_tmp[i3, i4] = k_var
                glorot_nor = weights_shape[2]+weights_shape[3]
                for i3, i4 in edges_tmp.keys():
                    edges.append((i3+prefix_from, i4+prefix_to, (edges_tmp[i3, i4] * glorot_nor)))
                lim_node = i4+prefix_to


            prefix_from = prefix_to
                       
    G_a = nx.Graph()
    for i in range(lim_node+1):
        G_a.add_node(i)
    G_a.add_weighted_edges_from(edges)


    louvain_com_G_a_dic = community.best_partition(G_a, weight='weight', resolution=res)
    Q_G_a_py = community.modularity(louvain_com_G_a_dic, G_a, weight='weight')
    print("modularity:" + str(Q_G_a_py))

    louvain_com_G_a_py = [[] for i in range(max(louvain_com_G_a_dic.values())+1)]
    print("number of community:" + str(len(louvain_com_G_a_py)))

    for i in louvain_com_G_a_dic.keys():
        louvain_com_G_a_py[louvain_com_G_a_dic[i]].append(i)
    
    louvain_com_G_a = algorithms.louvain(G_a, weight='weight', resolution=res)


    return()

argvs = sys.argv
calc(argvs[1])




