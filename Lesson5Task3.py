from statistics import mean

with open("L2T3.txt", 'r', encoding='utf-8') as file_text:
    file_text.seek(0)
    salary = []
    i = 0
    for line in file_text:
        salary.append(float(line[line.index(" "):]))
        if float(line[line.index(" "):]) < 20000 and i == 0:
            print("Список сотрудников с зарплатой меньше 20 000 рублей:")
            print(line[:line.index(" ")])
            i += 1
        elif float(line[line.index(" "):]) < 20000 and i != 0:
            print(line[:line.index(" ")])
print(f'Средняя зарплата всех сотрудинков {mean(salary)}')
