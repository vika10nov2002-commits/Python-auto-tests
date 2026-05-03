def  check_temperature(temp):
    assert temp <= 50, "Температура выходит за  допустимые пределы"
    assert temp >= - 50, 'Температура выходит за  допустимые пределы'
    print('Температура в пределах нормы')
check_temperature(-55)