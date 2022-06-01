# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные
# о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
from statistics import mean
from json import dump

with open('l5t7.txt', "r", encoding='utf-8') as data:
    data.seek(0)
    dict_result1 = {}
    for line in data:
        list_line = line.split(" ")
        dict_result1[list_line[0]] = int(list_line[2]) - int(list_line[3])

list_avrg = []
for el in dict_result1:
    if dict_result1[el] > 0:
        list_avrg.append(dict_result1[el])

avrg_profit = mean(list_avrg)
result = [dict_result1, {"averege_profit": avrg_profit}]
print(result)
with open('result.json', 'w') as write_res:
    dump(result, write_res)
