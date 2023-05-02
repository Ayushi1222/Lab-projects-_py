import string
import random
num=string.digits
alpha_num=string.digits+string.ascii_letters
print("OTP GENERATOR!")
c=input("Enter 'an' for alphanumeric OTP or 'n' for OTP of digits only: ")
if c=='an':
    otp_ls=random.choices(alpha_num,k=6)
    otp=''.join(otp_ls)
    print(otp)
else:
    otp_ls=random.choices(num,k=6)
    otp=''.join(otp_ls)
    print(otp)
