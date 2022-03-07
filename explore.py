import re
import matplotlib as mpl

import dataset
import traceback

# base_path = 'opt/Malware-Project/BigDataset/IoTScenarios/'
# filepath_complement = '/bro/conn.log.labeled'

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
    
def parse_dict(dataset_dict, file):
    for item in dataset_dict[file]:
        print(item)

def analisys(atribute):
    total = sum([int(i[1]) for i in dataset_dict[datafile][atribute].items()])
    print('IPs unicos:', len(list(dataset_dict[datafile][atribute].items())))
    top_ip = max(list(filter(lambda k: k[1] > 5, list(dataset_dict[datafile][atribute].items()))), key=lambda k: k[1])
    print(f'IP {top_ip[0]} representa {round((top_ip[1]/total)*100, 2)}% das chamadas')

if __name__ == '__main__':
    try:

        datafile = 'test'
        # for datafile in dataset.filenames: # For each dataset file

        # with open(base_path+datafile+filepath_complement, 'r') as file:
        with open('conn.log.labeled', 'r') as file:
            for line in file: # for each line
                parse_line(datafile, line.split())

        # parse_dict(dataset_dict, datafile)
        print('Os atributos do dataset:')
        for k in fields_map.keys():
            print(f"{fields_map[k]}")
        print()
        print(f'Captura: \t {datafile}')
        analisys('id.orig_h')
        analisys('id.resp_h')
    except Exception as e_:
        traceback.print_exc()