#!/usr/bin/python3

import socket

def toPigLatin(word):
    return word

def main():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(('localhost', 2828))
        (data, (ip, port)) = s.recvfrom(1024)
        sentence = data.decode('UTF-8')
        result = ''
        for word in sentence:
            result += toPigLatin(word) + ' '
        s.sendto(bytes(result, 'UTF-8'), (ip, port))
        s.close()

if __name__ == "__main__": main()