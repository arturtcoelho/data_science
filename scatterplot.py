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

def enum_map(col, row):
    try:
        return enum_dict[col][row]
    except KeyError:
        return -1


fields=[
#'ts',
# 'uid',
# 'id.orig_h',
# 'id.orig_p',
# ('id.resp_h', enum_map),
('id.resp_p', enum_map),
# ('proto', enum_map),
# ('service', enum_map),
('duration', number_map),
('orig_bytes', number_map),
('resp_bytes', enum_map),
('conn_state', enum_map),
('local_orig', enum_map),
('local_resp', enum_map),
('missed_bytes', enum_map),
('history', enum_map),
('orig_pkts', number_map),
('orig_ip_bytes', number_map),
('resp_pkts', number_map),
('resp_ip_bytes', number_map),
('tunnel_parents', enum_map),
# 'label',
# 'detailed-label'
]

if __name__ == '__main__':
    '''
        Reads for every file in the dataset and generates a basic analysis for the data
    '''
    try:
        datafile = 'conn.log.labeled'
        df = pd.read_csv('conn.log.labeled', delim_whitespace=True, low_memory=False)
        df = df.iloc[::100, :]

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

        for field1, func1 in fields:
            print(field1)
            for field2, func2 in fields:
                print('-', field2)
                try:

                    if field1==field2:
                        continue
                    if field1 not in [f[0] for f in fields] or field2 not in [f[0] for f in fields]:
                        continue


                    def map_func(col, row, func):
                        return func(col, row)

                    plt.scatter(beg_df.applymap(lambda k: map_func(field1, k, func1))[field1], 
                                beg_df.applymap(lambda k: map_func(field2, k, func2))[field2], c='blue')

                    plt.scatter(mal_df.applymap(lambda k: map_func(field1, k, func1))[field1], 
                                mal_df.applymap(lambda k: map_func(field2, k, func2))[field2], c='red')

                    plt.xlabel(field1)
                    plt.ylabel(field2)
                    plt.savefig(f'./images/{field1}-{field2}.png')

                except Exception as e_:
                    traceback.print_exc()
                    print('error on', field1, field2)
                    continue

    except Exception as e_:
        traceback.print_exc()
