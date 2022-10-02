listt = ['1', '2', '3',
         '4', '5', '6',
         '7', '8', '9']
x0 = input('Выберите X или 0 ').lower()

while listt[0] == '1' or listt[1] == '2' or listt[2] == '3' or listt[3] == '4' \
        or listt[4] == '5' or listt[5] == '6' or listt[6] == '7' or listt[7] == '8' or listt[8] == '9':

    def choosesetpos(listt):
        positionxo = input(f'Куда поставить {x0}? ')
        if positionxo == '1':
            listt[0] = x0
        elif positionxo == '2':
            listt[1] = x0
        elif positionxo == '3':
            listt[2] = x0
        elif positionxo == '4':
            listt[3] = x0
        elif positionxo == '5':
            listt[4] = x0
        elif positionxo == '6':
            listt[5] = x0
        elif positionxo == '7':
            listt[6] = x0
        elif positionxo == '8':
            listt[7] = x0
        elif positionxo == '9':
            listt[8] = x0


    print(listt[0], '|', listt[1], '|', listt[2])
    print('—————————')
    print(listt[3], '|', listt[4], '|', listt[5])
    print('—————————')
    print(listt[6], '|', listt[7], '|', listt[8])

    if listt[0] == 'x' and listt[1] == 'x' and listt[2] == 'x' \
            or listt[3] == 'x' and listt[4] == 'x' and listt[5] == 'x' \
            or listt[6] == 'x' and listt[7] == 'x' and listt[8] == 'x' \
            or listt[0] == 'x' and listt[3] == 'x' and listt[6] == 'x' \
            or listt[1] == 'x' and listt[4] == 'x' and listt[7] == 'x' \
            or listt[2] == 'x' and listt[5] == 'x' and listt[8] == 'x' \
            or listt[0] == 'x' and listt[4] == 'x' and listt[8] == 'x' \
            or listt[2] == 'x' and listt[4] == 'x' and listt[6] == 'x':
        print('X ВЫИГРАЛ!')
        exit()
    elif listt[0] == '0' and listt[1] == '0' and listt[2] == '0' \
            or listt[3] == '0' and listt[4] == '0' and listt[5] == '0' \
            or listt[6] == '0' and listt[7] == '0' and listt[8] == '0' \
            or listt[0] == '0' and listt[3] == '0' and listt[6] == '0' \
            or listt[1] == '0' and listt[4] == '0' and listt[7] == '0' \
            or listt[2] == '0' and listt[5] == '0' and listt[8] == '0' \
            or listt[0] == '0' and listt[4] == '0' and listt[8] == '0' \
            or listt[2] == '0' and listt[4] == '0' and listt[6] == '0':
        print('0 ВЫИГРАЛ!')
        exit()
    choosesetpos(listt)
    if x0 == 'x':
        x0 = '0'
    else:
        x0 = 'x'
