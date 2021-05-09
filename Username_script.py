from encrypt import genwrite_key, get_key
from cryptography.fernet import Fernet
import csv
def Login(user):
    genwrite_key()
    i = 0
    flag = False
    usernames = csv.reader(open('users.csv', 'rt'),delimiter=',')

    while flag != True:
        user = input("Enter Username: ")
        for row in usernames:
            if user in row:
                Logged_in_user = user
                flag = True
                print(user)
                Row_num = usernames.line_num
                continue
    for i in range(0,4):
        password = input("enter password for"+ user +": ")
        Enc_password = password.encode()
        key = get_key()
        a = Fernet(key)
        encrypt_password = a.encrypt(Enc_password)
        for line in usernames:
            if line[0] == user and line[1] == encrypt_password:
                print("pass correct")
                continue


            else: 
                print("incorrect try again")
                break
    print("pass correct")


