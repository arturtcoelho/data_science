#!/usr/bin/env python3
''' 
Author: Artur Temporal Coelho
GRR20190471

This project can be found on: https://github.com/arturtcoelho/data_science
'''

import re
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression

import dataset
import traceback

fields=[
# "ts",
# "uid",
# "id.orig_h",
# "id.orig_p",
# "id.resp_h",
# "id.resp_p",
# "proto",
# "service",
"duration",
"orig_bytes",
"resp_bytes",
# "conn_state",
# "local_orig",
# "local_resp",
# "missed_bytes",
# "history",
"orig_pkts",
"orig_ip_bytes",
"resp_pkts",
"resp_ip_bytes",
# "tunnel_parents",
# "label",
# "detailed-label"
"protoenum",
"serviceenum",
"historyenum",
"conn_stateenum",
"tunnel_parentsenum",
]

if __name__ == '__main__':
    try:
        
        df = pd.read_csv('./parsed_34_80.csv')

        for col in df:
            mapping = {k: v for v, k in enumerate(df[col].unique())}
            df[col+'enum'] = df[col].map(mapping)

        print(df.filter(items=fields))

        array = df.filter(items=fields).to_numpy()
        array = np.nan_to_num(array)

        kmean = KMeans(n_clusters=2, random_state=0)
        y_kmeans = kmean.fit_predict(array)

        y_real = [1 if k=='Benign' else 0 for k in df.label]

        count_00 = 0
        count_01 = 0
        count_10 = 0
        count_11 = 0
        total = len(y_kmeans)
        for i in range(total):
            if y_kmeans[i] and y_real[i]:
                count_11 += 1
            elif not y_kmeans[i] and y_real[i]:
                count_01 += 1
            elif y_kmeans[i] and not y_real[i]:
                count_10 += 1
            else:
                count_00 += 1

        print('cluster 1', sum(y_kmeans))
        print('cluster 0', len(y_kmeans)-sum(y_kmeans))

        print(count_11, count_10)
        print(count_01, count_00)

        print(count_11/total, count_10/total)
        print(count_01/total, count_00/total)

        plt.scatter(array[:, 0], array[:, 1], c=y_kmeans, s=50, cmap='viridis')
        plt.show()
        plt.scatter(array[:, 0], array[:, 1], c=y_real, s=50, cmap='viridis')
        plt.show()

    except Exception as e_:
        traceback.print_exc()
