n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

first = arr[n - 1] //제일 큰 수를 저장
second = arr[n - 2] //두 번째로 큰 수를 저장
hap = 0 //합
isk = 0 /*
제일 큰 수를 연속해서 k번 더하고 두 번째로 큰 수를 1번 더하고 를 반복하기 때문에 
제일 큰 수를 연속해서 몇 번 더했는지 횟수 저장하는 변수. 
*/
for i in range(m):
    if (isk >= 0) and (isk < k): // 제일 큰 수가 k번 이하로 더해졌다면
        hap += first // 제일 큰 숫자를 합에 더하고
        isk += 1 //isk를 1 증가
    elif isk >= k:
        hap += second // 제일 큰 수가 연속해서 k번 더해진 상황이면 second를 더한다.
        isk = 0
print(hap)
