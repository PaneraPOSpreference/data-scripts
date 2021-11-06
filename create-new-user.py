import qrcode
qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=1, )
def newQR():
    for i in range(1,5):
        userID = str(i)
        qr.add_data(userID)
        qr.make(fit=True)
        img = qr.make_image(fill_color=('#3C1C00'))
        img.save('userCode' + userID + '.png')
        img.show()
        print('\nNew Code Generated')
    
newQR()
