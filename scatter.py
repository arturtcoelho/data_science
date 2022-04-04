#!/usr/bin/env python3
''' 
Author: Artur Temporal Coelho
GRR20190471

This project can be found on: https://github.com/arturtcoelho/data_science
'''

import re
import matplotlib.pyplot as plt
import pandas as pd
import numpy

import dataset
import traceback

fields=[
# "ts",
# "uid",
# "id.orig_h",
# "id.orig_p",
# "id.resp_h",
"id.resp_p",
"proto",
"service",
"duration",
"orig_bytes",
"resp_bytes",
"conn_state",
"local_orig",
"local_resp",
"missed_bytes",
"history",
"orig_pkts",
"orig_ip_bytes",
"resp_pkts",
"resp_ip_bytes",
"tunnel_parents",
"label",
"detailed-label"
]

if __name__ == '__main__':
    try:
        
        for file in dataset.filenames:
            df = pd.read_csv(f'./parsed_files/{file}')

            for col in df:
                if col not in fields:
                    df = df.drop(col, axis=1)

            print(df)
            df.to_csv('out.csv')

    except Exception as e_:
        traceback.print_exc()
