letter = input('input letter: ')
for linenum,line in enumerate(open('/home/alex/Desktop/lab-3.3.txt','r+')):
    if linenum>=0:
        a=line.strip()
        if a[-1]==letter:
            print (a[::-1])