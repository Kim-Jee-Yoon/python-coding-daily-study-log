# python-coding-study-log
My phython practice &amp; learning record

## 조건 필터링 개선 실습 – Day03

# 오늘의 문제
사용자에게 정수를 하나 입력받아,
1부터 그 숫자까지 중에서 다음 조건을 만족하는 숫자만 출력하세요:
3의 배수이거나 7의 배수이지만
3과 7의 공배수는 제외
#🎯 조건
input()으로 숫자 입력 받기
1부터 n까지 범위 순회
3의 배수 또는 7의 배수만 출력 (단, 3과 7의 공배수는 제외)
한 줄에 하나씩 출력

### 🎯 문제 개요
- 1부터 입력한 숫자까지 출력
- 조건: 3 또는 7의 배수는 출력, 단 공배수는 제외

### 🧠 사고 흐름 요약
- 초기에 조건이 겹치며 중복 출력 → continue로 제어
- 중첩 if → 예외 조건 먼저 분리하여 가독성 향상
- pass는 아무 동작도 하지 않음 → continue로 구조 제어 필요

### ✅ 최종 코드
```python
n = int(input("숫자를 입력하세요"))

for i in range(1, n + 1):
    if i % 3 == 0 and i % 7 == 0:
        continue
    if i % 3 == 0 or i % 7 == 0:
        print(i)```
