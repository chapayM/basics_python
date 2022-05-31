# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны
# заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

# dict_eng = {1: "One", 2: "Two", 3: "Three", 4: "Four"}
dict_rus = {1: "Один", 2: "Два", 3: "Три", 4: "Четыре"}

with open("L5T4_1.txt", 'r', encoding='utf-8') as file_text_eng:
    with open("L5T4_2.txt", 'w', encoding='utf-8') as file_text_rus:
        for line in file_text_eng:
            list_line_eng = line.split(" ")
            list_line_rus = list_line_eng.copy()
            list_line_rus[0] = dict_rus.get(int(list_line_eng[2]))
            list_line_rus[2] = str(int(list_line_eng[2]))
            str_rus = " ".join(list_line_rus)
            print(str_rus, file=file_text_rus)
