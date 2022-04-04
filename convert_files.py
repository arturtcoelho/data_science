#!/usr/bin/env python3
''' 
Author: Artur Temporal Coelho
GRR20190471

This project can be found on: https://github.com/arturtcoelho/data_science
'''

import os
import subprocess
import re
import matplotlib as mpl

import dataset
import traceback

## Temporary disabled for testing
base_path = '/home/coelho/data_science/opt/Malware-Project/BigDataset/IoTScenarios/'
filepath_complement = '/bro/conn.log.labeled'

if __name__ == '__main__':
    '''
        Reads for every file in the dataset and generates a basic analysis for the data
    '''
    try:

        for datafile in dataset.filenames: # For each dataset file

            filename = base_path+datafile+filepath_complement
            os.system(f"tr -s '[:blank:]' ',' < {filename} > /home/coelho/data_science/parsed_files/{datafile}")
            os.system(f"sed -i /^#/d /home/coelho/data_science/parsed_files/{datafile}")
            cmd = f"sed -i '1s/^/ts,uid,id.orig_h,id.orig_p,id.resp_h,id.resp_p,proto,service,duration,orig_bytes,resp_bytes,conn_state,local_orig,local_resp,missed_bytes,history,orig_pkts,orig_ip_bytes,resp_pkts,resp_ip_bytes,tunnel_parents,label,detailed-label\\n/' /home/coelho/data_science/parsed_files/{datafile}"
            os.system(cmd)
            os.system(f'mv /home/coelho/data_science/parsed_files/{datafile} /home/coelho/data_science/parsed_files/{datafile}.csv')
            os.system(f"sed -i 's/-//g' /home/coelho/data_science/parsed_files/{datafile}.csv")

            print(datafile)

    except Exception as e_:
        traceback.print_exc()