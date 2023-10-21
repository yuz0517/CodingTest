a = []
for i in range(9):
    a.append(int(input()))
print(max(a))
print(a.index(max(a))+1)

#.index()
#Input: 9개의 숫자 입력
#output: 첫 번째 줄에는 숫자를, 두 번째 줄에는 몇 번째에 위치했는지 출력
