import qrcode
import string
import random

def newQR():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=1, )
    userKeys = string.ascii_uppercase
    userKey = (''.join(random.choice(userKeys) for x in range(10)))
    print('\n' + userKey)
    qr.add_data(userKey)
    qr.make(fit=True)
    img = qr.make_image(fill_color=('black'))
    img.save('userCode' + str(i) + '.png')
    # img.show()
    print('\nNew Code Generated')

for i in range(1,7):       
    newQR()
