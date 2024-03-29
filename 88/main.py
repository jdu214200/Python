class Задачи:
    def __init__(self):
        self.список_задач = []

    def добавить_задачу(self, задача):
        self.список_задач.append(задача)

    def удалить_задачу(self, задача):
        if задача in self.список_задач:
            self.список_задач.remove(задача)
            print(f"Задача '{задача}' удалена.")
        else:
            print(f"Задачи '{задача}' нет в списке.")

    def просмотреть_задачи(self):
        print("Список задач:")
        for i, задача in enumerate(self.список_задач, 1):
            print(f"{i}. {задача}")


# Пример использования
задачи_пользователя = Задачи()

задачи_пользователя.добавить_задачу("Подготовить презентацию")
задачи_пользователя.добавить_задачу("Прочитать новую книгу")
задачи_пользователя.добавить_задачу("Сделать зарядку")

задачи_пользователя.просмотреть_задачи()

задачи_пользователя.удалить_задачу("Прочитать новую книгу")

задачи_пользователя.просмотреть_задачи()
