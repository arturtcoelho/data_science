#!/usr/bin/env python3
''' 
Author: Artur Temporal Coelho
GRR20190471

This project can be found on: https://github.com/arturtcoelho/data_science
'''

import re
import matplotlib.pyplot as plt
import pandas as pd

import dataset
import traceback

enum_dict = {}

def number_map(col, row):
    try:
        return float(row)
    except ValueError:
        return 0

fields=[
#'ts',
# 'uid',
# 'id.orig_h',
# 'id.orig_p',
# ('id.resp_h', enum_map),
'id.resp_p',
# ('proto', enum_map),
'service',
'duration',
'orig_bytes',
'resp_bytes',
'conn_state',
'local_orig',
'local_resp',
'missed_bytes',
'history',
'orig_pkts',
'orig_ip_bytes',
'resp_pkts',
'resp_ip_bytes',
'tunnel_parents',
# 'label',
# 'detailed-label'
]

def mask(df, f):
    return df[f(df)]

if __name__ == '__main__':
    '''
        Reads for every file in the dataset and generates a basic analysis for the data
    '''
    try:
        datafile = 'conn.log.labeled'
        df = pd.read_csv('conn.log.labeled', delim_whitespace=True, low_memory=False)
        df = df.iloc[::1000, :] # every n rows

        # make enum dict of enum fields
        for col in df:
            if str(col) not in [f[0] for f in fields]:
                continue

            for f in fields:
                if f[0] == col and f[1] != enum_map:
                    continue

            enum_dict[col] = {}

            count = 0
            for row in df[col]:
                enum_dict[col][row] = count
                count += 1

        mal_df = df.loc[df['label'] == 'Malicious']
        beg_df = df.loc[df['label'] == 'Benign']

        for col in mal_df:
            if col not in fields:
                continue
            for i, row in enumerate(df[col]):
                try:
                    row = float(row)
                except Exception:
                    try:
                        mal_df.drop(i*1000, axis=0)
                        continue
                    except Exception:
                        pass


        for col in beg_df:
            if col not in fields:
                continue
            for i, row in enumerate(df[col]):
                try:
                    row = float(row)
                except Exception:
                    try:
                        beg_df.drop(i*1000, axis=0)
                        continue
                    except Exception:
                        pass

        for field1 in fields:
            print(field1)
            for field2 in fields:
                print('-', field2)
                try:

                    if field1==field2:
                        continue
                    if field1 not in [f[0] for f in fields] or field2 not in [f[0] for f in fields]:
                        continue

                    def map_func(col, row, func):
                        return func(col, row)

                    begx = beg_df.applymap(lambda k: map_func(field1, k, number_map))[field1]
                    begy = beg_df.applymap(lambda k: map_func(field2, k, number_map))[field2]

                    plt.scatter(begx, begy, c='blue')

                    malx = mal_df.applymap(lambda k: map_func(field1, k, number_map))[field1]
                    maly = mal_df.applymap(lambda k: map_func(field2, k, number_map))[field2]
                    plt.scatter(malx, maly , c='red')

                    plt.xlabel(field1)
                    plt.ylabel(field2)
                    plt.savefig(f'./images/{field1}-{field2}.png')

                except Exception as e_:
                    traceback.print_exc()
                    print('error on', field1, field2)
                    continue

    except Exception as e_:
        traceback.print_exc()
