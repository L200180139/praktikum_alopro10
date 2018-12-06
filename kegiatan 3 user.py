import socket
def prisma:
    L = 2*luasalas+luasselimut
    return L
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50001))
s.listen(5)
print "Server sudah siap"
data = ''

while 1:
    komm, addr = s.accept()
    while data.lower() !='keluar':
        data = komm.recv(1024)
        print 'Pesan:', data
        if data.find("parameter") != -1:
            param, value = data.split("=")
            if param == "parameter1":
                r = float(value)
                x = value
                komm.send("Parameter dicatat")
        elif data=='hitung':
            komm.send('luas prisma {} adalah {}'.format(x, prisma(r)))
        else:
            komm.send('Tidak ada')
