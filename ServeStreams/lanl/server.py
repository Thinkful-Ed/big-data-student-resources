import argparse
import socket
import sys
import pandas as pd
import json
import os
from time import sleep

def get_flow_data(infile):
    df = pd.read_csv(infile)
    df.sort_values("Time", inplace=True)
    response = df.to_json(orient='records')
    return response

def send_flows_to_spark(http_resp, tcp_connection):
    obj = json.loads(http_resp)
    for line in obj:
        try:
            payload = json.dumps(line) + '\n'
            print(f"this line: {payload}")
            print(f"type: {type(payload)}")
            print(f"line length: {len(payload.encode())}")
            print(f"-------------------------")
            tcp_connection.send(payload.encode())
            sleep(0.1)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", 
            help="provide the name of a file to process", 
            type=str, default='netflow_d02tinyh.csv')
    args = parser.parse_args()

    TCP_IP = socket.gethostbyname(socket.gethostname())
    TCP_PORT = 9009

    file_to_send = os.getcwd() + '/' + args.file
    print(f"Host: {TCP_IP} :: Port {TCP_PORT} :: File {file_to_send}")

    conn = None
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)
    print("Waiting for TCP connection....")
    conn, addr = s.accept()
    print("Connected... Sending flows")
    try:
        resp = get_flow_data(file_to_send)
        send_flows_to_spark(resp, conn)
    finally:
        conn.close()
