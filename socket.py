#!/usr/bin/env python

import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("socket creado")
except:
        print("creacion de socket fallido error %s(err)")
#puerto default
port = 80

try:
    host_ip = socket.gethostbyname('www.google.com')
except:
    print("se produjo un error al resolver el host")
    sys.exit()
s.connect((host_ip,port))
print("el socket se ha conectado correctamente con google:"+"\ncon el puerto:",port)
