st = list(input())
result = 0
i=0



while i < len(st):

    if st[i] == 'c':
        if i+1 >= len(st):
            i+=1
            result+=1
        elif st[i+1]=='=' or st[i+1]=='-':
            result += 1
            i += 2
        else:
            result += 1
            i+= 1
            
    elif st[i] == 'd':
        if i+1==len(st):

            i+=1
            result+=1
        elif i+2 == len(st):
            if st[i+1]=='-':

                result+=1
                i+=2
            else :

                result+=1
                i+=1
        elif i+3 == len(st):
            if st[i+1]=='z'and st[i+2]=='=' :

                result += 1
                i += 3
            elif st[i+1]=='-':

                result+=1
                i+=2
            else :

                i+=1
                result+=1
        
        else:
            if st[i+1]=='z'and st[i+2]=='=' :

                result += 1
                i += 3
            elif st[i+1]=='-':
    
                result+=1
                i+=2
            
            else:
                result += 1
                i+=1
            
    elif st[i] == 'l':
        if i+1 >= len(st):
            i+=1
            result+=1
        elif st[i+1]=='j':
            result += 1
            i += 2
        else:
            i+=1
            result+=1
            
    elif st[i] == 'n':
        if i+1 >= len(st):
            i+=1
            result+=1
        elif st[i+1]=='j':
            result += 1
            i += 2
        else:
            i+=1
            result +=1
            
    elif st[i] == 's':
        if i+1 >= len(st):
            i+=1
            result+=1
        elif st[i+1]=='=':
            result += 1
            i += 2
        else:
            i+=1
            result +=1
    elif st[i] == 'z':
        if i+1 >= len(st):
            i+=1
            result+=1
        elif st[i+1]=='=':
            result += 1
            i += 2
        else:
            i+=1
            result+=1
    else :
        i+=1
        result += 1
        
        
print(result)
