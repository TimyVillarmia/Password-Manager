import math, random, smtplib
from cryptography.fernet import Fernet
import os




# for creating key file 
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()
'''


def key_load():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

#OTP generator
def generateOTP():
	string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	OTP = ""
	length = len(string)
	for i in range(6) :
		OTP += string[math.floor(random.random() * length)]
	return OTP

# variable declaration
msg = generateOTP()
key = key_load()
fer = Fernet(key)



# sending email via gmail 
def email_sending():
    s = smtplib.SMTP('smtp.gmail.com', 587) # syntax - smtpObj = smtplib.SMTP( [host [, port [, local_hostname]]] )
    s.starttls()
    s.login("sender_email", "sender_password")
    s.sendmail("sender_email", email_counter, msg) # syntax - s.sendmail([sender_email], {receiver_email], [msg])
    print("OTP sent successfuly")
    print("Kindly check you email")
    s.quit



       
def verify_OTP():
    while True:
        user_otp = input("Enter OTP: ")
        if user_otp == msg:
            print("Verification Complete")
            menu()
        else:
            print("Invalid OTP")
            continue
    


def add_mode():
    new_user = input("Enter username: ")
    new_pass = input("Enter password: ")
    f = open("password.txt", "a")
    f.write(new_user + "|"+ fer.encrypt(new_pass.encode()).decode())
    f.write("\n")
    f.close()

def view_mode():
    f = open("password.txt", "r")
    for line in f.readlines():
        data = line.rstrip()
        user, pwds = data.split("|")
        print("User:", user, "\nPass:",fer.decrypt(pwds.encode()).decode())
        print("\n")


     
def menu():
    while True:
        user_mode = input("Type [Add] to Add new password \nType [View] to view existing passwords \nType [X] to quit: \n").lower()
        if user_mode == "x":
            quit()
    
        if user_mode == "add":
            add_mode()
        elif user_mode == "view":
            view_mode()
        else:
            continue
    

while True:
        if os.stat("email.txt").st_size == 0: #check if email.txt file has an email 
            master_email = input("Enter Email: ")
            email_f = open("email.txt", "w")
            email_f.write(master_email)
            email_f.close()
        else:
            master_email = input("Verify Email: ")
            email_counter = ""
            email_f = open("email.txt", "r")
            for i in email_f.readlines():
                email_counter += i   

                if email_counter == master_email:
                    generateOTP()
                    email_sending()
                    verify_OTP()
                else:
                    print("Invalid email")
                    continue
                

            
    













    

    
      




