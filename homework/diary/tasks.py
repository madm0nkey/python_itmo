from diary import storage


def show_tasks():
    print('Вы выбрали действие "Вывести список задач"\n')


def add_task():
    print('Вы выбрали действие "Добавить задачу"\n')
    storage.add_task()


def edit_task():
    print('Вы выбрали действие "Отредактировать задачу"\n')


def close_task():
    print('Вы выбрали действие "Завершить задачу"\n')


def reopen_task():
    print('Вы выбрали действие "Начать задачу сначала"\n')


def exit_from_diary():
    print('Вы выбрали действие "Выход"\n')