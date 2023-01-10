# OTP VERIFICATION PROGRAM
import random
import pywhatkit
type_otp=input("Enter what kind of OTP you want? type Mixed or Number:")
digit_otp=int(input("Enter how much digit you want 4 or 6?"))
ph_no=input("Enter your whatsapp number:")
number=['0','1','2','3','4','5','6','7','8','9']
char=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def otp_gen(para1,para2):
    otp_val=""
    if para1=='Mixed' or para1=='mixed':
        for _ in range(digit_otp):
            otp_val+=random.choice(char)
    else:
        for _ in range(digit_otp):
            otp_val+=random.choice(number)
    return otp_val
verify=otp_gen(type_otp,digit_otp)
print(verify)
def send_otp(para3):
    hour=int(input("Enter the hour:"))
    minu=int(input("Enter the min:"))
    pywhatkit.sendwhatmsg(para3,f"your otp is {verify}",hour,minu)
    print("Successfully Sent OTP")
send_otp(ph_no)
verification=input("Enter the your otp:")
def verf(para4):
    if verify==para4:
        print("Verified OTP")
    else:
        print("Invalid OTP")
verf(verification)
