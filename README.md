# python-coding-study-log
My phython practice &amp; learning record

## 조건 필터링 개선 실습 – Day03

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
