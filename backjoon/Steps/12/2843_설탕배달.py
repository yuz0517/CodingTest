#2839

n=int(input())
sugar=0
remain=0
temp=n
three=0
threesugar=0
while temp>=0:
    if n-5 < 0 or n-3<0 or n<=0 or temp-5<0:
        break
    elif ((temp-5)%3)==0:
        sugar=sugar+1
        temp=temp-5
        three=temp
        threesugar=sugar
    else :
        temp = temp-5
        sugar=sugar+1


if n<=0:
    print(-1)
    
elif temp%3==0:
    sugar = sugar+int(temp/3)
    
    print(sugar)
else :
    if three==0 and int(n%3)==0:
        print(int(n/3))
  
    else:

        if three!=0:
 
            threesugar+=int(three/3)
            print(threesugar)
        else:
            print(-1)

