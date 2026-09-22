class Burger:
    # 클래스 변수 (모든 버거가 공유하는 데이터)
    total_burgers_sold = 0

    def __init__(self, name, price):
        self.name = name    # 인스턴스 변수
        self.price = price  # 인스턴스 변수
        Burger.total_burgers_sold += 1

    # 1. 인스턴스 메서드 (객체의 데이터를 사용)
    def description(self):
        return f"{self.name}의 가격은 {self.price}원입니다."

    # 2. 클래스 메서드 (클래스 변수를 사용)
    @classmethod
    def get_total_sales(cls):
        # cls는 Burger 클래스 자체를 가리킵니다.
        return f"오늘 판매된 총 버거 수는 {cls.total_burgers_sold}개입니다."

    # 3. 정적 메서드 (클래스/객체 데이터 모두 안 씀, 단순 계산용)
    @staticmethod
    def is_healthy(calories):
        # 입력받은 칼로리 값만 가지고 판단하는 독립적인 함수
        return calories < 500

    # 4. 매직 메서드 (print()로 객체를 출력할 때 작동 방식을 정의)
    def __str__(self):
        return f"[버거 객체: {self.name}]"


# --- 클래스 함수들 활용하기 ---

# 객체 생성
burger1 = Burger("치즈버거", 5000)
burger2 = Burger("치킨버거", 6000)

# 1. 인스턴스 메서드 호출 (객체 이름으로 호출)
print(burger1.description())  # 출력: 치즈버거의 가격은 5000원입니다.

# 2. 클래스 메서드 호출 (클래스 이름으로 호출)
print(Burger.get_total_sales())  # 출력: 오늘 판매된 총 버거 수는 2개입니다.

# 3. 정적 메서드 호출 (클래스 이름으로 호출)
print(Burger.is_healthy(450))  # 출력: True

# 4. 매직 메서드 확인 (객체를 그냥 출력하거나 문자열로 변환할 때 자동 실행)
print(burger1)  # 출력: [버거 객체: 치즈버거]
