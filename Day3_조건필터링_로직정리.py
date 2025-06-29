n1 = int(input("숫자를 입력하세요"))

for x in range(1, n1+1):
    if x % 3 == 0 and x % 7 == 0:
        continue
    if x % 3 == 0 or x % 7 == 0:
        print(x)
