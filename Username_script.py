def Login(user):
    i = 0
    for i in range(0,4):
        flag = False
        usernames = open('users.txt', 'r')
        while flag != True:
            for line in usernames:
                if user in line:
                    Logged_in_user = user
                    usernames.close()
                    flag = True
                    print(user)
                    break
            
                else:
                    user = input("Insert username")
                    i = i+1
                    continue


def Password(password):
    import base64
    Dec_password = password.encode('ascii')
    Enc_password = base64.b64encode(Dec_password)
    


          
