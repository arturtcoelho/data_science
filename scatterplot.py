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

fields=[
#'ts',
# 'uid',
# 'id.orig_h',
# 'id.orig_p',
# 'id.resp_h',
# 'id.resp_p',
# 'proto',
# 'service',
'duration',
# 'orig_bytes',
# 'resp_bytes',
# 'conn_state',
# 'local_orig',
# 'local_resp',
# 'missed_byteshistory',
# 'orig_pkts',
# 'orig_ip_bytes',
'resp_pkts',
# 'resp_ip_bytes',
# 'tunnel_parents',
# 'label',
# 'detailed-label'
]

def map_val(val):
    try:
        return float(val)
    except ValueError:
        return 0


if __name__ == '__main__':
    '''
        Reads for every file in the dataset and generates a basic analysis for the data
    '''
    try:
        datafile = 'conn.log.labeled'
        df = pd.read_csv('conn.log.labeled', delim_whitespace=True, low_memory=False)
        mal_df = df.loc[df['label'] == 'Malicious']
        beg_df = df.loc[df['label'] == 'Benign']

        # for i in fields:
        #     for j in fields:
        i = fields[0]
        j = fields[1]
        print(i)
        print(j)
        plt.scatter(mal_df.applymap(map_val)[i], mal_df.applymap(map_val)[j], c='red')
        plt.scatter(beg_df.applymap(map_val)[i], beg_df.applymap(map_val)[j], c='blue')
        plt.xlabel(i)
        plt.ylabel(j)
        # plt.savefig(f'./images/{i}_{j}.png')
        plt.show()

    except Exception as e_:
        traceback.print_exc()
