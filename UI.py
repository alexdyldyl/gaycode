import random
from crypt import encrypt,decrypt,keygen,constructkey,getdic
while True:
    dic = getdic()
    print(dic)
    mssage = input()  
    ky = keygen()
    print(ky)
    kyy = input()
    typ = input()
    if typ==1:
        encrypt(kyy, mssage, dic)
    else:
        decrypt(mssage,kyy, dic)
