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

import dataset
import traceback

import pandas
import random

if __name__ == '__main__':
    '''
        Reads for every file in the dataset and generates a basic analysis for the data
    '''
    try:

        for datafile in dataset.filenames: # For each dataset file

            try:

                filename = f'/home/coelho/data_science/parsed_files/{datafile}.csv'
                
                p = 0.01 # % of lines
                df = pd.read_csv( filename, header=0, skiprows=lambda i: i>0 and random.random() > p)

                df.to_csv('sample01.csv', mode='a', header=False, index=False)

            except Exception:
                continue

    except Exception as e_:
        traceback.print_exc()