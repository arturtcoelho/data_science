import re

from attr import fields
import dataset
import traceback

base_path = 'opt/Malware-Project/BigDataset/IoTScenarios/'
filepath_complement = '/bro/conn.log.labeled'

fields_map = None
dataset_dict = {}

def generate_fields_map(line):
    global fields_map
    if fields_map != None:
        return

    m = {}
    for i, field in enumerate(line[1:]):
        m[i] = field

    fields_map = m

def parse_line(file, line):
    if file not in dataset_dict:
        dataset_dict[file] = []

    if line[0][0] == '#':
        if '#fields' in line:
            generate_fields_map(line)
        return
    
    dataset_dict[file].append({fields_map[i]:line[i] for i, field in enumerate(line)})
    # do some stuff with this
    
if __name__ == '__main__':
    try:

        for datafile in dataset.filenames: # For each dataset file

            with open(base_path+datafile+filepath_complement, 'r') as file:
                for line in file: # for each line
                    parse_line(datafile, line.split())

            print('FILE:\t', datafile, len(dataset_dict[datafile]))
    except Exception as e_:
        traceback.print_exc()