while True:
    from data_provider import get_choice
    def match_choice():
        match get_choice():
            case '1':
                import input_confirm as ic
                print(ic.confirm())
            case '2':
                import db_search
            case '3':
                from db_delete import delete
            case '4':
                exit()
    match_choice()