"""
Требуется создать csv-файл «rows_300.csv» со следующими столбцами:

– № - номер по порядку (от 1 до 300);
– Секунда – текущая секунда на вашем ПК;
– Микросекунда – текущая миллисекунда на часах.

На каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды.
Для работы с файлами подобного текстового формата потребуется встроенная в Python библиотека csv.

"""

import csv
import time
import datetime

# time
for i in range(1, 301):
    seconds = (str(time.time()).split(".")[0])[-1]
    mseconds = (str(time.time()).split(".")[1])[0] + (str(time.time()).split(".")[1])[1]
    # print(seconds)
    # print(mseconds)
    with open("../data/rows_300.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                i,
                seconds,
                mseconds
            )
        )
    time.sleep(0.01)

# datetime
with open("../data/rows_300_1.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(
        (
            'line',
            'Seconds',
            'Microseconds'
        )
    )
    for line in range(1, 301):
        writer.writerow(
            (
                line,
                datetime.datetime.now().second,
                datetime.datetime.now().microsecond
            )
        )

        time.sleep(0.01)
