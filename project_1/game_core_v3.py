def game_core_v3(value: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    #список чисел в котором будем искать искомое
    a = list(range(1,101))
    #переменные обозначающие ,левый индекс масссива и правый,а также число попыток
    left = 0
    right = len(a) - 1
    count = 0
    if type(value) != int:
        raise ValueError('Неверный ввод!')
    #запускаем цикл, в котором сравниваем искомое число с a[center], если value > a[center] то
    #ищем число в правой части массива,в противном случае в левой,после чего повторяем алгоритм
    while left <= right:
        count += 1
        center = (left + right) // 2
        if value == a[center]:
            break
        if value > a[center]:
            left = center + 1
        else:
            right = center - 1
    else:
        raise ValueError('значение отсутствует')
        
    # Ваш код заканчивается здесь

    return count