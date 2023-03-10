# Проект 0. Угадай число

## Оглавление  
[1. Описание проекта](.README.md#Описание-проекта)  
[2. Какой кейс решаем?](.README.md#Какой-кейс-решаем)  
[3. Краткая информация о данных](.README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](.README.md#Этапы-работы-над-проектом)  
[5. Результат](.README.md#Результат)    
[6. Выводы](.README.md#Выводы) 

### Описание проекта    
Угадать загаданное компьютером число за минимальное число попыток.

:arrow_up:[к оглавлению](_)


### Какой кейс решаем?    
Нужно написать программу, которая угадывает число за минимальное число попыток

**Условия соревнования:**  
- Компьютер загадывает целое число от 0 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число».
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества**     
Результаты оцениваются по среднему количеству попыток при 1000 повторений

**Что практикуем**     
Учимся писать хороший код на python


### Краткая информация о данных
Если совсем коротко, у нас есть одно случайное число между единицей и сотней :D
  
:arrow_up:[к оглавлению](.README.md#Оглавление)


### Этапы работы над проектом  
1. Создаем "песочную" версию игры, где угадывать рандомно заданное число необходимо нам самим: оформляем код в файле [game.py](https://github.com/khav-i/sf_data_science/blob/main/project_0/game.py) 
2. Пишем код для "прокаченной" версии игры, которая позволяет нам передать наш нелегкий труд по угадыванию заданного хитрым компуктером числа - самому компуктеру! Оформляем код в файле [game_v2.py](https://github.com/khav-i/sf_data_science/blob/main/project_0/game_v2.py)
3. Финальный! Ловко дописываем алгоритм и помогаем компьютеру найти заданное самим же собой число в 10 РАЗ БЫСТРЕЕ!

:arrow_up:[к оглавлению](.README.md#Оглавление)


### Результаты:  
Удалось добиться 10-КРАТНОГО ускорения поиска тайнственного числа! Раньше алгоритм пассивно перебирал значения на всём диапазоне, но теперь он реагирует на подсказки и ищет там, где "теплее".

:arrow_up:[к оглавлению](.README.md#Оглавление)


### Выводы:  
Как же прекрасно, когда благодаря внесению мелкого новшества в код удаётся ускорить его работу на порядок!

:arrow_up:[к оглавлению](.README.md#Оглавление)


