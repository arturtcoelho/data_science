#Artur Temporal Coelho
#GRR20190471 BCC

#https://github.com/arturtcoelho/data_science

from scapy.all import rdpcap, IP, TCP, UDP

packets = rdpcap('trace.pcap')

num_packages = len(packets)
num_ip = 0
num_tcp = 0
num_udp = 0
num_non_ip = 0

exec_errors = 0

tcp_sessions = {}
udp_sessions = {}

for p in packets:
    try:
        # p.show()

        src_ip = None
        dst_ip = None

        src_port = None
        dst_port = None

        if IP in p:
            num_ip += 1
            src_ip = p[IP].src
            dst_ip = p[IP].dst
        else:
            num_non_ip += 1
        
        if TCP in p:
            num_tcp += 1
            src_port = p[TCP].sport
            dst_port = p[TCP].dport
            ip_tuple = (src_ip, src_port, dst_ip, dst_port)
            reverse_ip_tuple = (dst_ip, dst_port, src_ip, src_port)

            if ip_tuple in tcp_sessions:
                tcp_sessions[ip_tuple].append(p)
            elif reverse_ip_tuple in tcp_sessions:
                tcp_sessions[reverse_ip_tuple].append(p)
            else:
                tcp_sessions[reverse_ip_tuple] = [p]

        elif UDP in p:
            num_udp += 1
            src_port = p[UDP].sport
            dst_port = p[UDP].dport
            ip_tuple = (src_ip, src_port, dst_ip, dst_port)
            reverse_ip_tuple = (dst_ip, dst_port, src_ip, src_port)
            
            if ip_tuple in udp_sessions:
                udp_sessions[ip_tuple].append(p)
            elif reverse_ip_tuple in udp_sessions:
                udp_sessions[reverse_ip_tuple].append(p)
            else:
                udp_sessions[reverse_ip_tuple] = [p]

    except Exception as e_:
        exec_errors += 1
        continue

print("Numero de pacotes", num_packages)
print("Numero de pacotes IP", num_ip)
print("Numero de pacotes TCP", num_tcp)
print("Numero de pacotes UDP", num_udp)
print("Numero de sessões TCP", len(tcp_sessions.items()))
print("Numero de sessões UDP", len(udp_sessions.items()))
print("Numero de pacotes não IP", num_non_ip)
print("Numero de erros", exec_errors)