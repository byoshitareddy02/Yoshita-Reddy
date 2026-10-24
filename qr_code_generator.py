import qrcode
url = input("Enter URL : ")
file_path = "C:\\Users\\byosh\\Visual studio\\python.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("QR is generated")