import ipfshttpclient
import pyqrcode
import qrcode
import image
import cv2
import pathlib
from PIL import Image
client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001/http')
res = client.add('D:\Blockchain\Mr.Vigneshwaran.N.pdf')
hash_value=res['Hash']
text_file = open("D:\Blockchain\data.txt", "w")
text_file.write(hash_value)
text_file.close()
print(hash_value)
f = open("data.txt","r")
im = Image.open(r"D:\Blockchain\certificate.png")
im.show() 
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data( hash_value)
qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color="black")
img.save("certificate.png")




client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001/http')
res = client.add('D:\Blockchain\Mr.Vigneshwaran.N.pdf')
get_hash_value=res['Hash']
if(get_hash_value==hash_value):
    print("QRcode is generated")
else:
    print("QRcode is not generated")
        


