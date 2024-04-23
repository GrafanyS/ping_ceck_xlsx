# import os
# import subprocess


# def ping_check(host):
#     return subprocess.run(['ping', '-c', '1', host], capture_output=True).returncode == 0


# def check_ping_list():
#     with open('ping_list.txt', 'r') as file:
#         for line in file:
#             host = line.strip()
#             if ping_check(host):
#                 print(f'{host} is up')
#             else:
#                 print(f'{host} is down')


# if __name__ == '__main__':
#     check_ping_list()

# import os
# import subprocess
# import socket

# def ping_check(host):
#     return subprocess.run(['ping', '-c', '1', host], capture_output=True).returncode == 0

# def sock_check(host, port=80):
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     # sock.settimeout(1)  # Timeout of 1 second
#     result = sock.connect_ex((host, port))
#     sock.close()
#     return result == 0

# def check_ping_and_sock_list():
#     with open('/home/valetovav/GIT/ping_excel_list/pythonProject/pingchecklist/ping_list.txt', 'r') as file:
#         for line in file:
#             parts = line.strip().split(':')
#             host = parts[0]
#             port = int(parts[1]) if len(parts) > 1 else 80  # Default to port 80 if not specified
#             ping_result = ping_check(host)
#             sock_result = sock_check(host, port)
#             print(f'{host}:{port} - Ping: {"up" if ping_result else "down"}, Socket: {"open" if sock_result else "closed"}')

# if __name__ == '__main__':
#     check_ping_and_sock_list()

import os
import subprocess
import socket
import time  # Import the time module

def ping_check(host):
    return subprocess.run(['ping', '-c', '1', host], capture_output=True).returncode == 0

def sock_check(host, port=80):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Timeout of 1 second
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0

def check_ping_and_sock_list():
    start_time = time.time()  # Record the start time
    ping_list = 'pythonProject/pingchecklist/ping_list.txt'
    # sock_list = []
    with open(ping_list, 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            host = parts[0]
            port = int(parts[1]) if len(parts) > 1 else 80  # Default to port 80 if not specified
            ping_result = ping_check(host)
            sock_result = sock_check(host, port)
            print(f'{host}:{port} - Ping: {"up" if ping_result else "down"}, Socket: {"open" if sock_result else "closed"}')
    end_time = time.time()  # Record the end time
    print(f'Total time taken: {end_time - start_time} seconds')

if __name__ == '__main__':
    check_ping_and_sock_list()