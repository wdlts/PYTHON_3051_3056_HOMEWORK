from data_provider import get_choice
while True:
    def match_choice():
        match get_choice():
            case '1':
                import input_confirm as ic
                print(ic.confirm())
            case '2':
                from db_search import search
            case '3':
                from db_delete import delete
            case '4':
                exit()
    match_choice()