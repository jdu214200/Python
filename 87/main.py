class ФинансовыйУчет:
    def __init__(self):
        self.доходы = []
        self.расходы = []

    def добавить_доход(self, сумма, описание):
        self.доходы.append({'сумма': сумма, 'описание': описание})

    def добавить_расход(self, сумма, описание):
        self.расходы.append({'сумма': сумма, 'описание': описание})

    def получить_баланс(self):
        общий_доход = sum(поступление['сумма'] for поступление in self.доходы)
        общий_расход = sum(расход['сумма'] for расход in self.расходы)
        баланс = общий_доход - общий_расход
        return баланс

    def показать_историю(self):
        print("Доходы:")
        for поступление in self.доходы:
            print(f"{поступление['описание']}: {поступление['сумма']}")
        print("\nРасходы:")
        for расход in self.расходы:
            print(f"{расход['описание']}: {расход['сумма']}")


# Пример использования
учет = ФинансовыйУчет()

учет.добавить_доход(1000, "Заработная плата")
учет.добавить_расход(300, "Продукты")
учет.добавить_расход(50, "Транспорт")

баланс = учет.получить_баланс()
учет.показать_историю()

print("\nОбщий баланс:", баланс)
