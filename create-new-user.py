import qrcode

def newQR():
    for i in range(1,4):
        userID = i
        img = qrcode.make(userID)
        img.save('userCode.png')
        img.show()
        print('\nNew Code Generated')
    
newQR()
    # userPreferences = input("\nEnter USERID: ")
    # img = qrcode.make(userPreferences)