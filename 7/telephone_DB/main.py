choice = input('Для внесения данных в базу введите 1, для поиска по базе введите 2 ')

match choice:
    case '1':
        import input_confirm as ic
        print(ic.confirm())
    case '2':
        import db_search
