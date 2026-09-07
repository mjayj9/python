class Calculator:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def add(self):
        return self.n1 + self.n2


# 객체 생성
calc = Calculator(10, 20)
# 메서드 호출
print(calc.add())  # 출력: 30
