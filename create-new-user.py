import qrcode
import string
import random
from flask import Flask

# function to create new code using qrcode library
# https://pypi.org/project/qrcode/
def newQR():
    
    # this QRCode class is where we can set our parameters such as the error correction
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=1, )
    
    # generate a random 10 character uppercase string as userKey
    userKeys = string.ascii_uppercase
    userKey = (''.join(random.choice(userKeys) for x in range(10)))
    
    # check the userKey looks okay and print them in Terminal for easy viewing.
    print('\n' + userKey)
    
    # to add the userKey data to our code we merely call the built in add_data function 
    # provided in the qrcode library
    qr.add_data(userKey)
    qr.make(fit=True)
    
    # we originally thought we'd try styling the codes with both Panera's logo and color
    # pallet but had the most consistent success with our code reading script when using 
    # black codes on a white background
    img = qr.make_image(fill_color=('black'))
    
    # saves each qr code in the current directory with file name corresponding to range provided in for loop
    img.save('userCode' + userKey + '.png')
    
    # check codes look okay, opens each in new window
    img.show()
    print('\nNew Code Generated')
      
newQR()

