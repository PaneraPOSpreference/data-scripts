import qrcode
from PIL import Image

def newQR():
    for i in range(1,5):
        userID = str(i)
        
        qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=1, )

        qr.add_data(userID)
        logo = Image.open('paneraLogo.png')
        img = qr.make_image().convert('RGB')
        pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
        img.paste(logo, pos)
        img.save('userCode' + userID + '.png')
        img.show()
        print('\nNew Code Generated')
    
newQR()
