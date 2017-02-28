# sudo pip install qrcode (comando para instalar módulo)
import qrcode
for n in range(1500):
    url = 'http://172.16.42.118/prueba/ver.php?cod=' + str(n+1)
    img = qrcode.make(url)
    path = './qr/' + str(n+1) + '.png'
    img.save(path)
