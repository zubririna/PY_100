from typing import Union, List, Tuple


def build_field(size: int, empty_cell: str = " ") -> list[list]:
    """
    Функция создаёт и возвращает пустое поле заданного размера, но не рисует его
    :param size: размер поля
    :param empty_cell: чем заполняется пустая ячейка
    :return: список списков, список "строк" поля
    """
    field = []     # заводим пустой список
    for row in range(size):    # строим каждую "строку" поля
        field.append([empty_cell]*size)     # добавляем пустую ячейку поля в строку в соответствии с размером поля
    return field


def draw_field(field: list[list]) -> None:
    """
    Функция рисует поле, изначально пустое, с оформленными границами ячеек
    :param field: поле, [[], ...], список списков
    :return: None
    """
    for row in field:    # в цикле по количеству строк
        for cell in row:    # обрабатываем в строке каждую ячейку поля
            print(f"|{cell}", end="")    # прорисовываем границы каждой ячейки поля. не переносим строку
        print("|")    # "закрываем" последнюю ячейку в строке поля


def get_int_val(text: str, border: int = None) -> int:
    """
    Функция проверяет вводимое значение и возвращает целое число,
    проверяет, входит ли значение в диапазон, ограниченный размером поля
    :param text: вводимое игроком значение, необязательно int
    :param border: допустимая граница диапазона вводимого значения (size-1)
    :return: вводимое игроком значение, координату строки или столбца
    """
    while True:
        val = input(text)    # ввод значения игроком
        try:
            val = int(val)
        except ValueError:
            print("Должно быть целым числом, попробуйте ещё раз")
            continue
        if border is not None:
            if not 0 <= val <= border:
                print(f"Значение должно лежать в диапазоне (0, {border}), попробуйте ещё раз")
                continue
        return val


def get_char_val(text: str, req_list: list) -> int:
    """
    Проверяет, что ввел игрок, и возвращает строку из допустимого списка элементов
    :param text: вводимый игроком символ (например, для идентификации игрока, чем обозначается его ход, Х или О)
    :param req_list: допустимые варианты символов
    :return: вводимый игроком символ
    """
    while True:
        val = input(text)
        if val not in req_list:
            print(f"Значение должно лежать в {req_list}")
            continue
        return val


def get_index_from_table(field: list[list], size: int) -> tuple[int, int]:
    """
    Функция запрашивает у игрока координаты ячейки, в которую он бы хотел поместить свой символ,
    проверяет, свободна ли данная ячейка
    :param field: имеющееся на данный момент игры поле
    :param size: заданный размер поля
    :return: координаты ячейки, куда будет совершен ход текущим игроком, если она свободна
    """
    while True:
        index_row = get_int_val("Введите индекс строки\n", size - 1)
        index_col = get_int_val("Введите индекс столбца\n", size - 1)
        if field[index_row][index_col] != " ":
            print("Ячейка занята, попробуйте другие координаты")
            continue
        break

    return index_row, index_col


def set_player_in_field(field: list[list], current_player: str, index_row: int, index_col: int) -> list[list]:
    """
    Ставит игрока на поле для совершения хода
    :param field: имеющееся на данный момент игры поле
    :param current_player: текущий игрок, тот, чей ход сейчас
    :param index_row: координата в строке
    :param index_col: координата в столбце
    :return: новое отрисованное поле со сделанным только что ходом
    """
    field[index_row][index_col] = current_player
    return field


def is_win(field: list[list], size: int) -> bool:
    """
    Функция определяет, произошла ли победа одного из игроков
    :param size: размер поля
    :param field: поле с совершенными на данный момент ходами для анализа
    :return: результат в виде логической переменной
    """
    flag_win = 0

    # проверка выигрыша по горизонтали
    for row in field:
        if row ==['X'] * size or row ==['O'] * size:   # равна ли строка заданной последовательности символов
            flag_win = 1

    # проверка выигрыша по вертикали
    for index_col in range(size):
        count_ver_X = 0
        count_ver_O = 0
        for i in range(size):
            if field[i][index_col] == 'X':
                count_ver_X +=1
            elif field[i][index_col] == 'O':
                count_ver_O += 1
        if count_ver_X == size or count_ver_O == size:
            flag_win = 1


    # проверка выигрыша по диагонали (левый верхний - правый нижний углы)
    count_dia_X = 0
    count_dia_O = 0
    for i in range(size):
        if field[i][i] == 'X':
            count_dia_X += 1
        elif field[i][i] == 'O':
            count_dia_O += 1
    if count_dia_X == size or count_dia_O == size:
        flag_win = 1

    # проверка выигрыша по диагонали (левый нижний - правый верхний углы)
    count_dia_X = 0
    count_dia_O = 0
    for i in range(size):
        if field[i][size-1-i] == 'X':
            count_dia_X += 1
        elif field[i][size-1-i] == 'O':
            count_dia_O += 1
    if count_dia_X == size or count_dia_O == size:
        flag_win = 1

    if flag_win == 1:
        return True
    else:
        return False


def change_player(player: str) -> str:
    """
    Функция меняет игрока, передает следующий ход сопернику
    :param player: текущий игрок на поле
    :return: выбор соперника, переход хода
    """
    new_player = "X" if player == "0" else "0"
    return new_player


def game(field: list[list], player: str, size: int) -> Union[str, None]:
    """
    Функция запускает непосредственно саму игру
    :param field: текущее поле
    :param player: текущий игрок
    :param size: заданный размер поля
    :return: -
    """
    current_player = player
    count_step = 0                  # счетчик ходов
    build_field(size)               # рисуем пустое поле
    while count_step < size*size:   # пока есть куда ходить
        print(f"Сейчас ставит игрок {current_player}")
        index_row, index_col = get_index_from_table(field, size) # получить индексы куда поставил игрок
        field = set_player_in_field(field, current_player, index_row, index_col) # ставим игрока на поле
        count_step += 1             # обновление  счетчика
        draw_field(field)           # рисуем поле после очередного хода
        if is_win(field, size):
            print(f"Победил игрок {current_player}")
            return current_player
        current_player = change_player(current_player)

    print("Ничья")
    return None


def app():
    """
    Запуск всего приложения
    :return: -
    """
    size = get_int_val("Введи размер поля\n")   # запрашиваем у игрока размер желаемого поля
    field = build_field(size)                   # строим поле, но не выводим его
    player = get_char_val("Кто первым ходит? X или 0\n", ["X","0"])       # выбор первого игрока по его символу
    flag_game = get_char_val("С кем играем? h или c\n", ["h","c"])        # выбор партнера: human or comp
    if flag_game == "h":
        game(field, player, size)               # запуск игры при выборе партнера - человека
    else:
        print("В разработке")                   # пока нет возможности играть с компьютером


if __name__ == "__main__":
    app()

