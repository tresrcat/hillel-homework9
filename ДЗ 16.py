class DiscountCalculator:
    def calculate_discount(self, price: float, is_vip: bool) -> float:
        if not is_vip:
            return price
        elif price < 1000:
            return price * 0.9
        else:
            return price * 0.8
calc = DiscountCalculator()
#1
assert calc.calculate_discount(100, is_vip=False) == 100
#2
assert calc.calculate_discount(100, is_vip=True) == 90.0
#3
assert calc.calculate_discount(1000, is_vip=True) == 800.0
print("Все тесты успешно пройдены!")
