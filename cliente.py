import socket as s

port = int(input("Porta: "))
c = s.socket(s.AF_INET, s.SOCK_STREAM)
c.connect(("nsa",port))
c.send('ack!'.encode())

r = c.recv(1024)

print(r)
