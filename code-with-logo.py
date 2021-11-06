from MyQR import myqr
import string
import random

for i in range(1,7):
    userKeys = string.ascii_uppercase
    userKey = (''.join(random.choice(userKeys) for x in range(10)))
    userID = ('USERID: ' + str(userKey))
    myqr.run(words = userID,
    version = 6,
    picture = 'paneraLogo.png',
    colorized = False,
    save_name = 'userIDcode' + str(i) + '.png')
    print('\nAdded New Code')