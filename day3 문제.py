# 오늘의 문제

#사용자에게 정수를 하나 입력받아,
#1부터 그 숫자까지 중에서 다음 조건을 만족하는 숫자만 출력하세요:
#3의 배수이거나 7의 배수이지만
#3과 7의 공배수는 제외
#🎯 조건
# input()으로 숫자 입력 받기

#1부터 n까지 범위 순회

#3의 배수 또는 7의 배수만 출력 (단, 3과 7의 공배수는 제외)

#한 줄에 하나씩 출력

#N = input("숫자를 입력해주세요")
#n = int(N)

#result = []
#for i in range (1, n+1):
    #keyNum = i % 3== 0 or i % 5== 0
    #if keyNum == (i % 3 ==0 and i % 5==0):
        #pass
    #result.append(keyNum)

#print(result)

#결과가 [False, False, True...] 이런 식으로 나와서 다시 풀기
##keyNum이 True, False로 나와서 문제임.
#N = input("숫자를 입력해주세요")
#n = int(N)

#result = []
#for i in range (1, n+1):
    #if  i % 3== 0 or i % 7== 0:
        #result.append(i)
        #if i % 3 ==0 and i % 7==0:
            #result.remove(i)
    
#print(result)

#%%문제 잘못 읽었네.. 한 줄 씩 출력해야지. 문제 파악부터 제대로/ 리스트를 빼자.
N = input("숫자를 입력해주세요")
n = int(N)

for i in range (1, n+1):
    if  i % 3== 0 or i % 7== 0:
        if i % 3 ==0 and i % 7==0:
            continue
        print(i)
        

#%%개선한 답
n1 = int(input("숫자를 입력하세요"))

for x in range(1, n1+1):
    if x % 3 == 0 and x % 7 == 0:
        continue
    if x % 3 == 0 or x % 7 == 0:
        print(x)
