from MyQR import myqr

for i in range(1,5):
    userID = str(i)
    myqr.run(words = userID,
    version = 6,
    picture = 'paneraLogo.png',
    colorized = True,
    save_name = 'userIDcode' + userID + '.png')
    print('\nAdded New Code')