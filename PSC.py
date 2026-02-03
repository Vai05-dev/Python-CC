Text=input("Enter Text :")
SpecialChr='''~!@#$%^&*()_+=-`{|}/ ?][":<'>;/.,'''
length=len(Text)
lc=uc=dc=sc=0
for c in Text:
    if c.islower():
        lc+=1
    elif c.isupper():
        uc+=1
    elif c.isdigit():
        dc+=1
    elif c in SpecialChr:
        sc+=1

score=0
if length>=7:
    score+=1
if lc>=2:
    score+=1
if uc>=2:
    score+=2
elif 0<uc<2:
    score+=1
if dc>=2:
    score+=2
elif 0<dc<2:
    score+=1
if sc>1:
    score+=1

if score>=6:
    if length>=12:
        print("Strong")
    elif 12>length>=8:
        print("Good")
    else:
        print("weak")
elif 4<score<6:
    print("Okay")
else:
    print("Bad")