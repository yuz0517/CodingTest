N = int(input())

ar=[]
result=0
for i in range(N):
  ar.append(input())

for i in ar:
    word=[]
    dic={}
    group=1
    word=list(i)
    print(word)
    for j in range(len(word)):
        if word[j] not in dic:
            print("처음 등장하는 문자! dic에 추가한다.")
            dic[word[j]] = 0
        elif word[j] in dic and word[j-1]==word[j]:
            print("현재 위치의 문자와 이전 문자가 같고 이 문자는 이미 등장한 문자이다.",word[j-1],word[j])
            print("group:1")
        elif word[j] in dic and word[j-1] != word[j]:
            print("이 문자는 이미 등장한 문자이며, -1위치의 문자와 다르다. 연속해서 나오지 않았기 때문에 그룹단어가 아니다. ",word[j-1],word[j])
            print("그룹단어 조건이 깨졌습니")
            group=0
        
    if group==1 :
        result +=1
        print(i,"는","그룹단어다. ")
    elif group==0:
        print(i,"는","그룹단어가 아닙니다.")
    print(dic)
print("result)
