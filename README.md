# data_science
## O Dataset
O dataset utilizado foi o IOT dataset do laboratorio estratosferico de Praga
https://www.stratosphereips.org/datasets-iot23
Esse dataset consiste de trafico de rede em equipamentos de IOT,
capturados entre 2018 e 2019, sendo eles rotulados de acordo com o tipo de ataque

Ele esta organizado em 20 capturas com conexões maliciosas e 3 capturas puramente benignas

No total são 106Gb de dados, e foram utilizadas apenas algumas capturas por vez para cada analise

### dataset.py
Contem os nomes de arquivos do dataset

### explore.py
Faz a leitura dos arquivos de log do dataset e realiza algumas analises

### parse_pcap.py
O arquivo conta_sessoes.py lê um arquivo .pcap, com as informações lidas da rede, e conta o numero de sessões e seus tipos
