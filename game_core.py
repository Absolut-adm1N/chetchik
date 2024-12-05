import numpy as np

def game_core_v3(number: int = 1) -> int:
    count  = 0
    start = 1
    stop = 101

    while True:
        average_number = (start + stop)//2
        count+=1
        if average_number == number:
            break
        elif number > average_number:
            start = average_number
        else:
            stop = average_number

    return count

def score_game(random_predict) -> int:
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")

score_game(game_core_v3)