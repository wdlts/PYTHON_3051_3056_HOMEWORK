# 2. # Иван решил создать самый большой словарь в мире.
# Для этого он придумал функцию biggest_dict(**kwargs),
# которая принимает неограниченное количество параметров «ключ: значение» и
# обновляет созданный им словарь my_dict, состоящий всего из одного элемента
# «first_one» со значением «we can do it». Воссоздайте эту функцию.

def biggest_dict(**kw):
    dictt = {}
    my_dict = {'first_one': 'we can do it'}
    my_dict.update(kw)
    while True:
        k = input('Input k')
        if k == '':
            break
        v = input('Input v')
        dictt[k] = v
    my_dict.update(dictt)
    print(my_dict)
biggest_dict(a=2, b=3, c=4, d=5)