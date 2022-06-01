f = open('text.txt', 'w', encoding='utf-8')
str_f='0'
while str_f!='':
    str_f = input('Введите строку для записи в файл. Для прекращения работы оставте ввод пустым:')
    if str_f=='':
       break
    else:
        print(str_f, file=f)
f.close()