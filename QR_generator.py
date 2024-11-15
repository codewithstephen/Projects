import qrcode
data = "www.careercredentials.in"
qr = qrcode.make(data, version = 1, box_size = 10, border = 2)
qr.save("my_code.png")
print("QR generated, see your current directory")