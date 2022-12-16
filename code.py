 import os
import random
import validators
import qrcode
import itertools
import calendar
import time
import os
import shutil
import wikipedia
import openpyxl as xl


def countdown(time_sec):
    for sec in range(1, time_sec+1):
        print(time_sec)
        time.sleep(1)
        time_sec -= 1
    print("Stop")
def timefind():
    curr_time = time.strftime("%H:%M:%S", time.localtime())
    print(curr_time)
def write(text): 
    print(text)
def add(a1, a2):
    print(int(a1) + int(a2))
def subtract(s1, s2):
    print(int(s1) - int(s2))
def multiply(m1, m2):
    print(int(m1) * int(m2))
def divide(d1, d2):
    print(int(d1) / int(d2))
def modulus(mo1, mo2):
    print(int(mo1) % int(mo2))
def power(p1, p2):
    print(int(p1)**int(p2))
def compare(c1, c2):
    if c1 < c2:
        print(int(c1), '<', int(c2))
    if c1 > c2:
        print(int(c1), '>', int(c2))
    if c1 == c2:
        print(int(c1), '=', int(c2))
def Round(rnum):
    print(round(rnum))
def binary(bnum):
    print(bin(bnum))
def low(ltext):
    print(ltext.lower())
def up(utext):
    print(utext.upper())
def spliter(sentence):
    split_list = sentence.split()
    for x in split_list:
        print(x)
def swap(swap_sentence):
    print(swap_sentence.swapcase())
def capitalise(word):
    print(word.capitalize())
def counting(fsent, cword):
    print(fsent.count(cword))
def div_mod(dm1, dm2):
    splited = divmod(dm1, dm2)
    for i in splited:
        print(i)
def hexa(hnum):
    print(hex(hnum))
def octa(onum):
    print(oct(onum))
def passgen():
    upcase1 = chr(random.randint(65, 90))
    lowcase1 = chr(random.randint(65, 90)).lower()
    lowcase2 = chr(random.randint(65, 90)).lower()
    lowcase3 = chr(random.randint(65, 90)).lower()
    passnumlist = list(range(0, 9))
    num1 = int(random.choice(passnumlist))
    num2 = int(random.choice(passnumlist))
    num3 = int(random.choice(passnumlist))
    passsymlist = ['@', '!', '#', '$', '%', '&', '*', '?']
    sym1 = random.choice(passsymlist)
    password = (upcase1 + lowcase1 + lowcase2 + lowcase3 + str(num1) + str(num2)
                 + str(num3) + sym1)
    print('The generated password is :', password)
def countlet(csent):
    count = 0
    for i in range(0, len(csent)):
      count += 1
    print(count)
def percent(pnum1, pnum2):
    pernum = str(pnum1)
    per = float(int(((pnum1))) / float(int((pnum2)))) * 100
    print(str(per) + '%')
def isup(utxt):
    print(utxt.isupper())
def islow(ltxt):
    print(ltxt.islower())
def istit(ttxt):
    print(ttxt.istitle())
def isdec(dnum):
    print(dnum.isdecimal())
def isnum(nnum):
    print(nnum.isnumeric())
def valiurl(urlstr):
    if validators.url(urlstr) == True:
        print('This is a valid URL.')
    else:
        print('This is not a valid URL.')
def rolldice():
    print('The number is', random.randint(1, 6))
def repl(rsen, rwrd1, rwrd2):
    print(rsen.replace(rwrd1, rwrd2))
def lastlet(llsent):
    llist = llsent.split()
    llist.reverse()
    print('The last letter of this word or sentence is', llist[0])
def lstgen(lgtxt):
    lst = []
    while True:
      worl = input('How to split? word-wise or letter-wise : ').lower()
      if worl == 'word':
          print(lgtxt.split())
          break
      elif worl == 'letter':
          for each_letter in lgtxt:
              lst.append(each_letter)
          print(lst)
          break
      else:
          continue
def crefile(src, filename, ext):
    os.chdir(src)
    open((filename + ext), 'w')
    print('File created')
def editfile(edfilename, edtxt):
    text_file = open(edfilename, "r")
    data = text_file.read()
    text_file.close()
    edit = open(edfilename, 'w')
    edit.write(data + edtxt)
def createqr(qrtxt, qrname):
    qr_img = qrcode.make(qrtxt)  
    qr_img.save(qrname + ".jpg")
    print(f'QR code of data {qrtxt} is saved as {qrname}.jpg')
def isPalindrome(s):
    return s == s[::-1]
def readfile(fnme):
    with open(fnme, 'r') as file:
        for line in file:
            print(line)
def primenumber(pnum):
    for Number in range (1, pnum+1):
        count = 0
        for i in range(2, (Number//2 + 1)):
            if(Number % i == 0):
                count = count + 1
                break
        if (count == 0 and Number != 1):
            print(Number, end=' ')
def square_root(srnum):
    newrootnum = srnum ** 0.5
    print(f'Square root of {srnum} is {newrootnum}')
def randomnum(fromnum, tonum):
    print('Your random number is :', random.randint(fromnum, tonum))
def multable(mtnum):
    for i in range(1, 16):
        print(mtnum, 'x', i, '=', mtnum*i)
def shufcrds():
    deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))
    random.shuffle(deck)
    print("You got:")
    for i in range(10):
        print(deck[i][0], "of", deck[i][1])
def monthcalendfind(yy, mm):
    print(calendar.month(yy, mm))
def yearcalendfind(yy):
    print(calendar.calendar(yy))
def savemoncalend(yy, mm, src, name):
    os.chdir(src)
    open(name + '.txt', 'w+')
    edit = open(name + '.txt', 'w')
    edit.write(calendar.month(yy, mm))
    print(f'Saved calender of month {mm} in the year of {yy} as {name}')
def saveyearcalend(yy, src, name):
    os.chdir(src)
    open(name + '.txt', 'w+')
    edit = open(name + '.txt', 'w')
    edit.write(calendar.calendar(yy))
    print(f'Saved calender of year {yy} as {name}')
def movefile(src, des, copyorcut):
    while copyorcut != 'copy' or 'move':
        allfiles = os.listdir(src)
        if copyorcut == 'copy':
            for f in allfiles:
                src_path = os.path.join(src, f)
                des_path = os.path.join(des, f)
                shutil.copy(src_path, des_path)
                print(f'{f} copied')
            break
        elif copyorcut == 'move':
            for f in allfiles:
                src_path = os.path.join(src, f)
                des_path = os.path.join(des, f)
                shutil.move(src_path, des_path)
                print(f'{f} moved')
            break
        else:
            copyorcut = input('Copy or move file :').lower()
            continue
def delfold(dir):
    shutil.rmtree(dir)
    print('Folder deleted successfully')
def delfile(dire):
    for f in os.listdir(dire):
        if f == '.ipynb_checkpoints':
            continue
        else:
            os.remove(os.path.join(dire, f))
        print(f'{f} deleted')
def factors(num):
    print("The factors of", num, "are:")
    for i in range(1, num + 1):
       if num % i == 0:
           print(i)
def crefold(src, name):
    os.mkdir(f'{src}/{name}')
    print('Folder created')
def istriangle(s1, s2, s3):
    if (s1 + s2 >= s3) and (s2 + s3 >= s1) and (s3 + s1 >= s2):
        print('It is a valid triangle')
    else:
        print('It is not a valid triangle')
def editxl(filename, sheetname, cell, cellvalue):
    wb = xl.load_workbook(filename)
    sheet = wb.get_sheet_by_name(sheetname)
    sheet[cell] = cellvalue
    wb.save(filename)

print(
    'Hi Welcome to Viper, a programming language exclusively made for beginners.'
)

finc = ''

email = input('Enter email : ').lower()
password = input('Enter password : ')
email_list = [
    'tharun@viper.com', 'sappiea@viper.com', 'tesla@viper.com', 'chitti@viper.com', 'lmes@viper.com'
]
pass_list = [
    'tharun@123', 'sappia@123', 'tesla@123', 'chitti@123', 'lmes@123'
]

while True:
    for eml in email_list:
        for passwrd in pass_list:
            if email == eml and password == passwrd:
                status = True
                print('You can start using Viper.')
                while finc != 'end':
                    finc = input('>>> ').lower()
                    if finc == 'write':
                        try:
                            write(input('Enter text to write : '))
                        except ValueError:
                            print(
                                'Error : Enter number instead of any other values')
                    elif finc == 'edit excel':
                        try:
                            editxl(input('Enter excel file name : '), input('Enter sheet name : '), input('Enter cell name : '), input('Enter cell value : '))
                        except FileNotFoundError:
                            print('Error : File not found')
                    elif finc == 'is triangle':
                        try:
                            istriangle(float(input('Enter side 1 length : ')),
                                       float(input('Enter side 2 length : ')),
                                       float(input('Enter side 3 length : ')))
                        except ValueError:
                            print('Enter number instead of other values')
                    elif finc == 'create folder':
                        try:
                            crefold(input('Enter source for creating folder : '),
                                    input('Enter folder name : '))
                        except IsADirectoryError:
                            print('Error : Is this a directory')
                        except NotADirectoryError:
                            print('Error : This is not a directory')
                    elif finc == 'find factors':
                        try:
                            factors(int(input('Enter number for factors : ')))
                        except ValueError:
                            print('Error : Enter number instead of other values')
                    elif finc == 'delete files':
                        try:
                            delfile(input('Enter source for file : '))
                        except FileNotFoundError:
                            print('Error : File not found')
                        except IsADirectoryError:
                            print('Error : Is this a directory')
                        except NotADirectoryError:
                            print('Error : This is not a directory')
                    elif finc == 'timer':
                        countdown(int(input('Enter seconds for timer : ')))
                    elif finc == 'move files':
                        try:
                            movefile(input('Enter source for file : '),
                                     input('Enter file destination : '),
                                     input('Copy or move file : ').lower())
                        except FileNotFoundError:
                            print('Error : File not found')
                        except IsADirectoryError:
                            print('Error : Is this a directory')
                        except NotADirectoryError:
                            print('Error : This is not a directory')
                    elif finc == 'delete folder':
                        try:
                            delfold(input('Enter source for folder : '))
                        except FileNotFoundError:
                            print('Error : File not found')
                        except IsADirectoryError:
                            print('Error : Is this a directory')
                        except NotADirectoryError:
                            print('Error : This is not a directory')
                    elif finc == 'generate random number':
                        try:
                            randomnum(int(input('Number from : ')),
                                      int(input('To : ')))
                        except ValueError:
                            print('Error : Enter a number instead of other values')
                    elif finc == 'show time':
                        timefind()
                    elif finc == 'shuffle cards':
                        shufcrds()
                    elif finc == 'multiplication table':
                        try:
                            multable(
                                int(
                                    input(
                                        'Enter number to show multiplication table : '
                                    )))
                        except ValueError:
                            print('Error : Enter a number instead of other values')
                    elif finc == 'is upper':
                        isup(input('Enter text to check if in upper case : '))
                    elif finc == 'is lower':
                        isup(input('Enter text to check if in lower case : '))
                    elif finc == 'is title':
                        istit(
                            input(
                                'Enter data to check if it follows all the rules of a title : '
                            ))
                    elif finc == 'is decimal':
                        isdec(input('Enter data to check if it is a decimal : '))
                    elif finc == 'is numeric':
                        isnum(input('Enter data to check if it is numeric : '))
                    elif finc == 'add':
                        try:
                            add(input('Number 1 : '), input('Number 2 : '))
                        except ValueError:
                            print('Error : Enter a number instead of other values')
                    elif finc == 'addition':
                        try:
                            add(input('Number 1 : '), input('Number 2 : '))
                        except ValueError:
                            print('Error : Enter a number instead of other values')
                    elif finc == 'subtract':
                        try:
                            subtract(input('Number 1 : '), input('Number 2 : '))
                        except ValueError:
                            print('Error : Enter a number instead of other values')
                    elif finc == 'sub':
                        try:
                            subtract(input('Number 1 : '), input('Number 2 : '))
                        except ValueError:
                            print('Error : Enter a number instead of other values')
                    elif finc == 'multiply':
                        try:
                            multiply(input('Number 1 : '), input('Number 2 : '))
                        except ValueError:
                            print('Error : Enter a number instead of other values')
                    elif finc == 'divide':
                        try:
                            divide(input('Number 1 : '), input('Number 2 : '))
                        except ValueError:
                            print('Error : Enter a number instead of other values')
                        except ZeroDivisionError:
                            print('Error : Cannot divide by 0')
                    elif finc == 'div':
                        try:
                            divide(input('Number 1 : '), input('Number 2 : '))
                        except ValueError:
                            print('Error : Enter a number instead of other values')
                        except ZeroDivisionError:
                            print('Error : Cannot divide by 0')
                    elif finc == 'mod':
                        try:
                            modulus(input('Number 1 : '), input('Number 2 : '))
                        except ValueError:
                            print('Error : Enter a number instead of other values')
                        except ZeroDivisionError:
                            print('Error : Cannot divide by 0')
                    elif finc == 'power':
                        try:
                            power(input('Base : '), input('Exponent : '))
                        except ValueError:
                            print('Error : Enter a number instead of other values')
                    elif finc == 'compare':
                        try:
                            compare(input('Number 1 : '), input('Number 2 : '))
                        except ValueError:
                            print('Error : Enter a number instead of other values')
                    elif finc == 'round':
                        try:
                            Round(float(input('Number : ')))
                        except ValueError:
                            print('Error : Enter a number instead of other values')
                    elif finc == 'round off':
                        try:
                            Round(float(input('Number : ')))
                        except ValueError:
                            print('Error : Enter a number instead of other values')
                    elif finc == 'convert to binary':
                        try:
                            binary(
                                int(input('Enter number to convert to binary : ')))
                        except ValueError:
                            print('Error : Enter a number instead of other values')
                    elif finc == 'lower':
                        low(input('Enter text to convert to lower case : '))
                    elif finc == 'upper':
                        up(input('Enter text to convert to upper case : '))
                    elif finc == 'split':
                        spliter(input('Enter sentence to split : '))
                    elif finc == 'swap case':
                        swap(input('Enter text to swap case : '))
                    elif finc == 'capitalize':
                        capitalise(
                            input('Enter text to capitalize first letter : '))
                    elif finc == 'count occurence':
                        counting(
                            input('Enter sentence : ').lower(),
                            input('Enter word to check times of occurence : ').
                            lower())
                    elif finc == 'abs':
                        try:
                            abs_inp = abs(float(input('Enter number for abs : ')))
                            print(abs_inp)
                        except ValueError:
                            print('Error : Enter number instead of any other values')
                    elif finc == 'divmod':
                        try:
                            div_mod(int(input('Number 1 : ')),
                                    int(input('Number 2 : ')))
                        except ZeroDivisionError:
                            print('Error : Cannot divide by 0')
                        except ValueError:
                            print('Error : Enter number instead of any other values')
                    elif finc == 'length':
                        lsent = len(
                            input(
                                'Enter a word or a sentence to check its length : '
                            ))
                        print(lsent)
                    elif finc == 'len':
                        lsent = len(
                            input(
                                'Enter a word or a sentence to check its length : '
                            ))
                        print(lsent)
                    elif finc == 'count letters':
                        countlet(
                            input(
                                'Enter a word or a sentence to count letters : '))
                    elif finc == 'convert to hexadecimal':
                        try:
                            hexa(
                                int(
                                    input(
                                        'Enter number to convert to hexadecimal : '
                                    )))
                        except ValueError:
                            print('Error : Enter a number instead of other values')
                    elif finc == 'convert to octal':
                        try:
                            octa(int(input('Enter number to convert to octal : ')))
                        except ValueError:
                            print('Error : Enter a number instead of other values')
                    elif finc == 'generate password':
                        passgen()
                    elif finc == 'password generator':
                        passgen()
                    elif finc == 'percentage calculator':
                        try:
                            percent(input('Percentage from : '),
                                    input(' is what % of : '))
                        except ValueError:
                            print('Error : Enter a number instead of other values')
                    elif finc == 'calculate percentage':
                        try:
                            percent(input('Number : '), input(' is what % of : '))
                        except ValueError:
                            print('Error : Enter a number instead of other values')
                    elif finc == 'url validator':
                        valiurl(input('Enter URL to validate : '))
                    elif finc == 'validate url':
                        valiurl(input('Enter URL to validate : '))
                    elif finc == 'roll dice':
                        rolldice()
                    elif finc == 'dice roll':
                        rolldice()
                    elif finc == 'replace':
                        repl(input('Enter Sentence : '),
                             input('Enter word to replace from : '),
                             input('Enter word to replace to : '))
                    elif finc == 'last word finder':
                        lastlet(input('Enter data to check last word : '))
                    elif finc == 'find last word':
                        lastlet(input('Enter data to check last word : '))
                    elif finc == 'last word finder':
                        lastlet(input('Enter data to check last word : '))
                    elif finc == 'list generator':
                        lstgen(input('Enter text to create as a list : '))
                    elif finc == 'generate list':
                        lstgen(input('Enter text to create as a list : '))
                    elif finc == 'create qr code':
                        createqr(input('Enter text to create a qr code : '),
                                 input('Enter name of the qr code : '))
                    elif finc == 'create qr':
                        createqr(input('Enter text to create a qr code : '),
                                 input('Enter name of the qr code : '))
                    elif finc == 'create file':
                        try:
                            crefile(
                                input('Enter source to create file : '),
                                input('Enter file name to create : '),
                                input(
                                    'Enter file extension(Ex:- .html, .py, etc...) : '
                                ))
                        except FileNotFoundError:
                            print("Error : Can't find source")
                    elif finc == 'edit file':
                        try:
                            editfile(input('Enter file name to open : '),
                                     input('Enter text to add to your file : '))
                        except FileNotFoundError:
                            print('Error : File not found')
                    elif finc == 'is palindrome':
                        s = input('Enter text to check for palindrome : ')
                        ans = isPalindrome(s)
                        if ans:
                            print("Yes")
                        else:
                            print("No")
                    elif finc == 'read file':
                        try:
                            readfile(
                                input(
                                    'Enter file name to print data(with extension) : '
                                ))
                        except FileNotFoundError:
                            print('Error : File not found')
                    elif finc == 'prime numbers finder':
                        try:
                            primenumber(
                                int(
                                    input(
                                        'Enter number to find prime numbers less than that : '
                                    )))
                        except ValueError:
                            print('Error : Enter a number instead of other values')
                    elif finc == 'find prime numbers':
                        try:
                            primenumber(
                                int(
                                    input(
                                        'Enter number to find prime numbers less than that : '
                                    )))
                        except ValueError:
                            print('Error : Enter a number instead of other values')
                    elif finc == 'find square root':
                        try:
                            square_root(
                                float(
                                    int(
                                        input(
                                            'Enter Number for finding square root : '
                                        ))))
                        except ValueError:
                            print('Error : Enter a number instead of other values')
                    elif finc == 'square root finder':
                        try:
                            square_root(
                                float(
                                    int(
                                        input(
                                            'Enter Number for finding square root : '
                                        ))))
                        except ValueError:
                            print('Error : Enter a number instead of other values')
                    elif finc == 'show monthly calender':
                        try:
                            monthcalendfind(int(input('Enter year : ')),
                                            int(input('Enter month number : ')))
                        except ValueError:
                            print('Error : Enter month or year properly')
                        except IndexError:
                            print('Error : Enter month or year properly')
                    elif finc == 'show yearly calender':
                        try:
                            yearcalendfind(int(input('Enter year : ')))
                        except ValueError:
                            print('Error : Enter year properly')
                        except IndexError:
                            print('Error : Enter year properly')
                    elif finc == 'save monthly calender':
                        try:
                            savemoncalend(int(input('Enter year : ')),
                                          int(input('Enter month : ')),
                                          input('Enter source to save : '),
                                          input('Enter name for file : '))
                        except ValueError:
                            print('Enter month or year properly')
                        except IsADirectoryError:
                            print('Error : Is this a directory')
                        except NotADirectoryError:
                            print('Error : This is not a directory')
                    elif finc == 'save yearly calender':
                        try:
                            saveyearcalend(int(input('Enter year : ')),
                                           input('Enter source to save : '),
                                           input('Enter name for file : '))
                        except ValueError:
                            print('Enter year properly')
                        except IsADirectoryError:
                            print('Error : Is this a directory')
                        except NotADirectoryError:
                            print('Error : This is not a directory')
                    elif finc == 'end':
                        print('The program has been ended')
                        quit()
                    else:
                        print('This is not a valid function.')
                break
            else:
                status = False
    if status == False:
        print('Access denied')
        email = input('Enter email : ').lower()
        password = input('Enter password : ')
        continue
