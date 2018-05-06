import random
import requests
NULLS = 10
dic = {}

sup = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ., 0123456789'
from textwrap import wrap

def getdic():
    r = requests.get('http://127.0.0.1:5000')
    s = r.text
    letters = wrap(sup,1)
    letters.append(' ')
    keys = wrap(s, 3)
    for letter in letters:
        num = letters.index(letter)
        dic[letter] = keys[num]
    return dic

def encrypt(ky, message, dic):
    codded = ''
    key = wrap(ky,3)
    mesz = ''
    for i in message:
        mesz += dic[i]
    mes = int(mesz)
    print(mes)
###########################################
    configuringmes = []
    m = wrap(str(mes), 3)
    glider = 1
    stri = ''
    justmes = ['0' for i in range(len(str(mes))//3 + len(key)-1)]
#print(justmes)

    for keysymbol in key:
        configuringmes = []
        for messagesymbol in m:
            rres = str(int(messagesymbol)*int(keysymbol))
            configuringmes.append(rres)
            #configuringmes.reverse()
        for i in range(len(key)-glider):
            configuringmes.append('0')
        configuringmes.reverse()
    #print(configuringmes)
        for i in range(len(configuringmes)):
            justmes[i] = str(int(justmes[i])+int(configuringmes[i]))
        glider = glider + 1
    justmes.reverse()
    for i in justmes:
        zzeros = '0'
        input_string = i
        string_len = len(input_string)
        for zz in range(1, NULLS - string_len, 1):
            zzeros = zzeros + '0'
        rres = zzeros + i
        stri +=rres
    print(stri)
    return stri
########################################


def decrypt(stri, ky, dic):


    key = wrap(ky,3)
    key.reverse()
    justmes = wrap(stri, NULLS)
    mes = []
    justmes.reverse()
    l = len(justmes) - len(key) + 1
    for i in range(l):
        m = int(justmes[0])/int(key[0])
        for k in range(len(key)):
            justmes[k] = str(int(justmes[k])-m*int(key[k]))
        mes.append(m)
        for j in justmes:
            if j=='0':
                justmes.remove(j)
    mes.reverse()
    message = ''

    for i in mes:
        for j in dic.keys():
            if dic[j] == str(i):
                message += str(j)


    print(message)
    return message


def keygen():
    s = ''
    for i in range(99):
        s += str(random.randint(100, 999))
    return s


def constructkey(s1, s2, attempt):
    key = ''
    if attempt%2 == 0:
        for i in range(48):
            key += s1[i] +s2[i]
    else:
        for i in range(48):
            key += s2[i] + s1[i]
    return key




