with open('shuf_60.csv', 'r') as f:
    l = f.readlines()


l = [x if x.split(',')[-1] != '\n' else x[:-1] + 'Benign\n' for x in l if x.split(',')[-1] != 'DDoS\n']
l = [x for x in l if x.split(',')[-1] != 'DDoS\n']

size = len(l)

with open('parsed_60_80.csv', 'w') as f:
    f.write(''.join(l[:int(size*0.8)]))

with open('parsed_60_20.csv', 'w') as f:
    f.write(''.join(l[int(size*0.8):]))