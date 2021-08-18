'''
Write functions to count number of characters,
number of words, number of upper case characters,
number of lower case characters, number of digits,
number of lines and number of spaces in a file. Write program for this.
'''
def countchar(fobj):
    data=fobj.read()
    count=0
    for ch in data:
        count=count+1
    return count
def countwords(fobj):
    data=fobj.readlines()
    count=0
    for lines in data:
        l1=lines.split()
        for words in l1:
            count=count+1
    return count
def countuchar(fobj):
    data=fobj.read()
    coutupper=0
    for ch in data:
        if ch.isupper():
            countupper+=1
    return countupper
def countlchar(fobj):
    data=fobj.read()
    countlower=0
    for ch in data:
        if ch.islower():
            countlower+=1
    return countlower
def countdigit(fobj):
    data=fobj.read()
    count=0
    for ch in data:
        if ch.isdigit():
            count+=1
    return count
def countlines(fobj):
    lines=fobj.readlines()
    count=0
    for l1 in lines:
        count+=1
    return count
def countspaces(fobj):
    data=fobj.read()
    count=0
    for l1 in data:
        if l1.isspace():
            count+=1
    return count
