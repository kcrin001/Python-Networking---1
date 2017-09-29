#!/usr/bin/python3

import socket


def toPigLatin(word):
    if word[0] is ('a' or 'e' or 'i' or 'o' or 'u'):
        result = word + 'ay'
    else:
        index = -1
        for i in range(len(word) - 1, 0, -1):
            if word[i] in ['a', 'e', 'i', 'o', 'u']:
                index = i
        result = word[index:] + word[0:index] + 'ay'
    return result.lower()


def main():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(('localhost', 2828))
        (data, (ip, port)) = s.recvfrom(1024)
        sentence = data.decode('UTF-8')
        result = ''
        for word in sentence.split():
            result += toPigLatin(word) + ' '
        s.sendto(bytes(result, 'UTF-8'), (ip, port))
        s.close()


if __name__ == "__main__": main()