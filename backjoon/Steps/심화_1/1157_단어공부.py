str = list(input())
dic = {}
result=0
maxl=''
for i in str:
    if i.upper() in dic:
        dic[i.upper()] = dic[i.upper()]+1
    else :
        dic[i.upper()]=0


maxvalue = max(dic.values())


for key, value in dic.items() :
    if value == maxvalue:
    
        result+=1
        maxl=key
if result != 1:
    print('?')
else:
    print(maxl)
