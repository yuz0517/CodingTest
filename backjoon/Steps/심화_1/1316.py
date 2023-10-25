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
    for j in range(len(word)):
        if word[j] not in dic:
      
            dic[word[j]] = 0
        elif word[j] in dic and word[j-1]==word[j]:
            continue
        elif word[j] in dic and word[j-1] != word[j]:
            group=0
        
    if group==1 :
        result +=1
        
print(result)
