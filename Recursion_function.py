def factorial(n):
    # 1. 종료 조건 (Base Case)
    if n <= 1:
        return 1
    
    # 2. 재귀 호출 (Recursive Case)
    return n * factorial(n - 1)

print(factorial(4))  # 출력: 24
