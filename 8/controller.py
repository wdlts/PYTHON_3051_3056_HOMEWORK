while True:
    from choice import get_choice

    choice = get_choice()
    match choice:
        case '1':
            import input as ic

            print(ic.confirm())
        case '2':
            from search_db import search

            print(search())
        case '3':
            from delete_data import delete

            print(delete())
        case '4':
            from search_db import search_null

            print(search_null())
        case '5':
            exit()
