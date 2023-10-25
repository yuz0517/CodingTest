ar=[]
totalscore=0
totalcredit=0
score=0
dic={'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0}

for i in range(20) :
    ar.append(input())

for i in ar:
    course=''
    credit=''
    grade=''
    j=[]
    j = i.split(' ')
    course = j[0]
    credit=j[1]
    grade=j[2]
    
    if grade=='P' :
        continue
    else :
        score=float(dic[grade])*float(credit)
        totalscore += score
        totalcredit+=float(credit)


print("{:.6f}".format(totalscore/totalcredit))
