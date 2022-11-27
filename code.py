import random
import validators
import qrcode
import itertools
import calendar

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
    password = (upcase1 + lowcase1 + lowcase2 + lowcase3 + str(num1) + str(num2) + str(num3) + sym1)
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
def crefile(filename, ext):
    open((filename + ext), 'w')
def editfile(edfilename, edtxt):
    text_file = open(edfilename, "r")
    data = text_file.read()
    text_file.close()
    edit = open(edfilename, 'w')
    edit.write(data + edtxt)
def createqr(qrtxt, qrname):
    qr_img = qrcode.make(qrtxt)  
    qr_img.save(qrname + ".jpg") 
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
    print(newrootnum)
def randomnum(fromnum, tonum):
    print(random.randint(fromnum, tonum))
def multable(mtnum):
    for i in range(1, 16):
        print(mtnum, 'x', i, '=', mtnum*i)
def shufcrds():
    deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))
    random.shuffle(deck)
    print("You got:")
    for i in range(5):
        print(deck[i][0], "of", deck[i][1])
def calendfind(yy, mm):
    print(calendar.month(yy, mm))


finc = ''

print('Hi Welcome to Viper, a programming language exclusively made for kids.')

while finc != 'end':
    finc = input('Viper Code > ').lower()
    if finc == 'write':
        write(input('Enter text to write : '))
    elif finc == 'generate random number':
        try:
            randomnum(int(input('Number from : ')), int(input('To : ')))
        except ValueError:
            print('Error : Enter a number instead of other values')
    elif finc == 'shuffle cards':
        shufcrds()
    elif finc == 'multiplication table':
        try:
            multable(int(input('Enter number to show multiplication table : ')))
        except ValueError:
            print('Error : Enter a number instead of other values')
    elif finc == 'is upper':
        isup(input('Enter text to check if in upper case : '))
    elif finc == 'is lower':
        isup(input('Enter text to check if in lower case : '))
    elif finc == 'is title':
        istit(input('Enter data to check if it follows all the rules of a title : '))
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
    elif finc == 'div':
        try:
            divide(input('Number 1 : '), input('Number 2 : '))
        except ValueError:
            print('Error : Enter a number instead of other values')
    elif finc == 'mod':
        try:
            modulus(input('Number 1 : '), input('Number 2 : '))
        except ValueError:
            print('Error : Enter a number instead of other values')
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
            binary(int(input('Enter number to convert to binary : ')))
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
        capitalise(input('Enter text to capitalize first letter : '))
    elif finc == 'count occurence':
        counting(input('Enter sentence : ').lower(), input('Enter word to check times of occurence : ').lower())
    elif finc == 'abs':
        abs_inp = abs(float(input('Enter number for abs : ')))
        print(abs_inp)
    elif finc == 'divmod':
        div_mod(int(input('Number 1 : ')),int(input('Number 2 : ')))
    elif finc == 'length':
        lsent = len(input('Enter a word or a sentence to check its length : '))
        print(lsent)
    elif finc == 'len':
        lsent = len(input('Enter a word or a sentence to check its length : '))
        print(lsent)
    elif finc == 'count letters':
        countlet(input('Enter a word or a sentence to count letters : '))
    elif finc == 'convert to hexadecimal':
        try:
            hexa(int(input('Enter number to convert to hexadecimal : ')))
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
            percent(input('Percentage from : '),input(' is what % of : '))
        except ValueError:
            print('Error : Enter a number instead of other values')
    elif finc == 'calculate percentage':
        try:
            percent(input('Number : '),input(' is what % of : '))
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
        repl(input('Enter Sentence : '), input('Enter word to replace from : '), input('Enter word to replace to : '))
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
        createqr(input('Enter text to create a qr code : '), input('Enter name of the qr code : '))
    elif finc == 'create qr':
        createqr(input('Enter text to create a qr code : '), input('Enter name of the qr code : '))
    elif finc == 'create file':
        crefile(input('Enter file name to create : '), input('Enter file extension(Ex:- .html, .py, etc...) : '))
    elif finc == 'edit file':
        try:
            editfile(input('Enter file name to open : '), input('Enter text to add to your file : '))
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
            readfile(input('Enter file name to print data(with extension) : '))
        except FileNotFoundError:
            print('Error : File not found')
    elif finc == 'prime numbers finder':
        try:
            primenumber(int(input('Enter number to find prime numbers less than that : ')))
        except ValueError:
            print('Error : Enter a number instead of other values')
    elif finc == 'find prime numbers':
        try:
            primenumber(int(input('Enter number to find prime numbers less than that : ')))
        except ValueError:
            print('Error : Enter a number instead of other values')
    elif finc == 'find square root':
        try:
            square_root(float(int(input('Enter Number for finding square root : '))))
        except ValueError:
            print('Error : Enter a number instead of other values')
    elif finc == 'square root finder':
        try:
            square_root(float(int(input('Enter Number for finding square root : '))))
        except ValueError:
            print('Error : Enter a number instead of other values')
    elif finc == 'show calender':
        try:
            calendfind(int(input('Enter year : ')), int(input('Enter month number : ')))
        except ValueError:
            print('Error : Enter month or year properly')
    elif finc == 'end':
        break
    else:
        print('This is not a valid function.')
