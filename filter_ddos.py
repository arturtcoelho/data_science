with open('parsed_files/CTU-IoT-Malware-Capture-1-1.csv', 'r') as f:
    l = f.readlines()

l = [x if x.split(',')[-1] != '\n' else x[:-1] + 'Benign\n' for x in l if x.split(',')[-1] != 'DDoS\n' and x.split(',')[-1] != 'PartOfAHorizontalPortScan\n']
l = [x for x in l if x.split(',')[-1] != 'DDoS\n']

with open('parsed_1.csv', 'w') as f:
    f.write(''.join(l))