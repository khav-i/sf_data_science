"""Игра 'Угадай число'.
Сам компьютер загадывает и сам угадывает
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    low_num = 1  # Предварительно задаем нижнюю границу поиска.
    up_num = 101  # Предварительно задаем верхнюю границу поиска.

    while True:
        count += 1
        predict_number = np.random.randint(low_num, up_num)  # Предполагаемое число.
        if predict_number > number:
            up_num = predict_number

        elif predict_number < number:
            low_num = predict_number
        
        elif number == predict_number:
            break  # Выход из цикла, если угадали.
    return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): Функция угадывания.

    Returns:
        int: Среднее количество попыток.
    """
    count_ls = []
    np.random.seed(1) # Фиксируем сид для воспроизводимости.
    random_array = np.random.randint(1, 101, size=(1000)) # Загадали список чисел.
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


if __name__ == '__main__':
    # RUN
    score_game(random_predict)
