#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def main():
    while True:
        sentence = input("Enter a sentence: ")
        s.sendto(bytes(sentence, 'UTF-8'), ('localhost', 2828))
        (data, (ip, port)) = s.recvfrom(1024)
        result = data.decode('UTF-8')
        print(result)

if __name__ == "__main__": main()