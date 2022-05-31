with open("L2T2.txt", 'r', encoding='utf-8') as file_text:
    file_text.seek(0)
    str_f = 0
    for line in file_text:
        str_f += 1
        words = line.count(" ") + 1
        print(f'Строка {str_f} содержит {words} слов')
print(f'Файл L2T2.txt содержит {str_f} строк')
