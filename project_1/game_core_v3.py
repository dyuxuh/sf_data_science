import numpy as np
def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    # Создаём переменные
    count = 0
    predict = 11
    predict_number = 1
    
    #запускаем цикл угадывания
    while number != predict_number:
        count+=1
        if number > predict:
            predict+= 10 
        predict_number =  np.random.randint(predict-10,predict)                    
    

    return count