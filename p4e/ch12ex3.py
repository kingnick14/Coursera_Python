# import socket
# try:
#     inp = input('Enter a URL:')
#     inpSocket = inp.split('/')
#
#     print(inpSocket[2])
#
#     mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     mysock.connect((inpSocket[2], 80))
#     cmd = str('GET ' + inp + ' HTTP/1.0\r\n\r\n').encode()
#     mysock.send(cmd)
#     dl = 0
#     while True:
#         data = mysock.recv(300)
#         dl = dl + len(data)
#         if len(data) < 1: break
#         elif dl <= 3000: print(data.decode(),end='')
#     print('\n\nnico:',dl)
#     mysock.close()
#
# except socket.gaierror:
#     print('Oops!  That was no valid URL.  Try again...')

import urllib.request


inp = urllib.request.urlopen(input('Enter a URL:'))
counts = dict()
count = 0
for line in inp:
    words = line.decode().split()
    for word in words:
        print(word)
        for chars in words:
            count = count + 1
            #if count < 3000: print(chars)
print(inp)
#print(len(inp))
print(count)

#     inpSocket = inp.split('/')
