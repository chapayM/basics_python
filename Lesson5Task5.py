# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
with open("L5T5.txt", 'w', encoding='utf-8') as file_num:
    num = 0
    while num != '':
        num = input('Введите число для записи в файл. Для прекращения работы поле пустым:')
        str_f = num + " "
        if num == '':
            break
        else:
            file_num.write(str_f)
with open("L5T5.txt", 'r', encoding='utf-8') as file_num:
    content = file_num.read().rstrip()
    content_list = [int(el) for el in content.split(" ")]
    print(sum(content_list))
