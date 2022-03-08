#!/usr/bin/env python3
''' 
Author: Artur Temporal Coelho
GRR20190471

This project can be found on: https://github.com/arturtcoelho/data_science
'''

import re
import matplotlib as mpl

import dataset
import traceback

## Temporary disabled for testing
# base_path = 'opt/Malware-Project/BigDataset/IoTScenarios/'
# filepath_complement = '/bro/conn.log.labeled'

fields_map = None
dataset_dict = {}

def generate_fields_map(line):
    '''
        Gets the field atributes
    '''
    global fields_map
    if fields_map != None:
        return

    m = {}
    for i, field in enumerate(line[1:]):
        m[i] = field

    fields_map = m

def parse_line(file, line):
    '''
        For each line of the log file add the count to the refering atribute and key
    '''
    if file not in dataset_dict:
        dataset_dict[file] = {}
        
    if line[0][0] == '#':
        if '#fields' in line:
            generate_fields_map(line)
            for _, field in fields_map.items():
                dataset_dict[file][field] = {}
        return    
    
    for i, field in enumerate(line):
        if field not in dataset_dict[file][fields_map[i]]:
            dataset_dict[file][fields_map[i]][field] = 1
        else:
            dataset_dict[file][fields_map[i]][field] += 1

def analisys(atribute):
    '''
        Print some basic data from each key, such as total of unique ocurrences 
        and how much the most common one represents of the total
    '''
    print()
    print(f'{atribute} - unique keys:', end='')
    # prints atribute and total size of unique samples
    total = sum([int(i[1]) for i in dataset_dict[datafile][atribute].items()])
    print(len(list(dataset_dict[datafile][atribute].items())))
    try:
        keys_list = list(filter(lambda k: k[1] > 0, list(dataset_dict[datafile][atribute].items())))
        top_ip = max(keys_list, key=lambda k: k[1])
        print(f"key '{top_ip[0]}' represents {round((top_ip[1]/total)*100, 2)}% of all keys")
    except ValueError:
        pass

if __name__ == '__main__':
    '''
        Reads for every file in the dataset and generates a basic analysis for the data
    '''
    try:

        datafile = 'conn.log.labeled' # Temp name for testing
        # for datafile in dataset.filenames: # For each dataset file

        # with open(base_path+datafile+filepath_complement, 'r') as file:
        with open('conn.log.labeled', 'r') as file: # Temp open only one of the files
            for line in file: # for each line
                parse_line(datafile, line.split())

        # Print data
        print('Dataset atributes:\n')
        for k in fields_map.keys():
            print(f"{fields_map[k]} ", end='')
        print()
        print()

        # Print each capture data
        print(f"Capture: \t {datafile} \t total size: {sum([int(i[1]) for i in dataset_dict[datafile]['ts'].items()])}")
        for item in fields_map.items():
            analisys(item[1])

    except Exception as e_:
        traceback.print_exc()
    
    ''' Comment:

        The info contained in the source file represents the data capture of IOT devices
        Each capture contains the same data format:
        (Roughly represented here)
        Timestamp, id, source ip, source port, destination ip, destination port, 
        protocol, service, duration, number of bytes, etc., in the end they are labeled as Begning or Malicious

        With a basic human analysis is possible to note some simple caractheristics in this capture (20-1)

        Only 3 addresses made calls in this capture, and 99.94% of them were made by a single one
        Of this single IP, there is a main port that was used to make calls

        40% of the calls were made to a single address

        99.47% of the calls are UDP

        Almost all of the calls are labeled as 'begnign'

        With a quick look on the source file its possible to note that the malicious calls were not 
        made by the main address + port combination, and were in fact made TO the same address + port combination
        This could tell us that a combined key of two ore more columns could be usefull to get a more in depht analysis

        The malicious calls are also made using tcp and no dns
    '''
