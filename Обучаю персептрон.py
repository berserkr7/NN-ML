import numpy as np

w = np.array([0, 0, 0]) # изначальные веса

examples = np.array([[1, 1, 0.3], [1, 0.4, 0.5], [1, 0.7, 0.8]])


def target(ex): # целевая
    if ex[0] == 1 and ex[1] == 1 and ex[2] == 0.3:
        return 1
    elif ex[0] == 1 and ex[1] == 0.4 and ex[2] == 0.5:
        return 1
    elif ex[0] == 1 and ex[1] == 0.7 and ex[2] == 0.8:
        return 0
    

def predict(ex): # предсказание
    summ = w.T @ ex
    print('Пример: ', ex)
    print('Сумматорная функция: ', summ)
    if summ > 0:
        return 1
    else:
        return 0
    

perfect = False # переменная отражает, что алгоритм будет работать до тех пор, пока все идеально не классифицируем
while not perfect:
    perfect = True # предполагаем, что уже идеально классифицируем примеры
    i = 0
    for e in examples:
        if predict(e) != target(e):
            perfect = False
            if predict(e) == 0:
                w = w + e
                print(f"{w} = {w} + {e} = {w + e}")
            elif predict(e) == 1:
                w = w - e
                print(f"{w} = {w} - {e} = {w - e}")
        i = i+1
        print(f'На шаге {i} получили w: ', w)
        print()
        print()
print('Итоговые веса:', w)