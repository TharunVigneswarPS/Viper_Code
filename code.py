import random
import validators

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
def split(sentence):
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


finc = ''

print('Hi Welcome to Viper, a programming language exclusively made for kids.')

while finc != 'end':
    finc = input('Viper Code > ').lower()
    if finc == 'write':
        write(input('Enter text to write : '))
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
        add(input('Number 1 : '), input('Number 2 : '))
    elif finc == 'addition':
        add(input('Number 1 : '), input('Number 2 : '))
    elif finc == 'subtract':
        subtract(input('Number 1 : '), input('Number 2 : '))
    elif finc == 'sub':
        subtract(input('Number 1 : '), input('Number 2 : '))
    elif finc == 'multiply':
        multiply(input('Number 1 : '), input('Number 2 : '))
    elif finc == 'divide':
        divide(input('Number 1 : '), input('Number 2 : '))
    elif finc == 'div':
        divide(input('Number 1 : '), input('Number 2 : '))
    elif finc == 'mod':
        modulus(input('Number 1 : '), input('Number 2 : '))
    elif finc == 'power':
        power(input('Base : '), input('Exponent : '))
    elif finc == 'compare':
        compare(input('Number 1 : '), input('Number 2 : '))
    elif finc == 'round':
        Round(float(input('Number : ')))
    elif finc == 'round off':
        Round(float(input('Number : ')))
    elif finc == 'convert to binary':
        binary(int(input('Enter number to convert to binary : ')))
    elif finc == 'lower':
        low(input('Enter text to convert to lower case : '))
    elif finc == 'upper':
        up(input('Enter text to convert to upper case : '))
    elif finc == 'split':
        split(input('Enter sentence to split : '))
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
        hexa(int(input('Enter number to convert to hexadecimal : ')))
    elif finc == 'convert to octal':
        octa(int(input('Enter number to convert to octal : ')))
    elif finc == 'generate password':
        passgen()
    elif finc == 'password generator':
        passgen()
    elif finc == 'percentage calculator':
        percent(input('Percentage from : '),input(' is what % of : '))
    elif finc == 'calculate percentage':
        percent(input('Number : '),input(' is what % of : '))
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
    elif finc == 'end':
        break
    else:
        print('This is not a valid function.')
