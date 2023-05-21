import copy


class StarCinema:
    _hall_list = []

    def _entry_hall(self, ot):
        self._hall_list.append(ot)


class Hall(StarCinema):
    def __init__(self, row, cols, hall_no):
        self.__seats = {}
        self.__show_list = []  # Event
        self.__row = row
        self.__cols = cols
        self.__hall_no = hall_no
        self._entry_hall(vars(self))

    def entry_show(self, id, movie_name, time):  # Event Add
        self.__show_list.append((id, movie_name, time))
        seat = [['Empty' for i in range(self.__row)]
                for j in range(self.__cols)]
        self.__seats[id] = seat

    def book_seats(self, customer_name, phone, id, list_of_tup):

        for key, val in self.__seats.items():
            if key == id:
                for ind, val2 in enumerate(val):
                    for ind2, val3 in enumerate(val2):
                        for ind3, val4 in enumerate(list_of_tup):
                            if val[ind][ind2] != 'Empty':
                                print(val)
                                return
            break
        for i in list_of_tup:
            if 1 < list_of_tup.count(i):
                print(
                    f'{"-"*100}\n>>>>>>YOUR ARE GIVVEN DUPLICATE SEAT PLEASE VALID SEAT NO TRY AGAIN \n{"-"*100}')
                return
        flag = 1
        is_booked = True
        for ids, _ in self.__seats.items():
            if ids == id:
                flag = 0
        is_done = True
        for i in list_of_tup:
            if self.__cols - 1 < i[0] or self.__row - 1 < i[1]:
                print(f'{"-"*100}\n>>>>>> SEATS LIMIT CROSSED\n{"-"*100}')
                is_done = False
                break
        if is_done and not flag:
            for key, value in self.__seats.items():
                if key == id:
                    for i in list_of_tup:
                        if value[i[0]][i[1]] != 'Empty':
                            print(
                                f'{"-"*100}\n>>>>>>>SEAT ARE ALREDAY BOOKED\n{"-"*100}')
                            break
                        else:
                            value[i[0]][i[1]] = customer_name
                            is_booked = False
                    break
        if not is_booked:
            show = []
            for i in self.__show_list:
                if i[0] == id:
                    show.append(i)
                    break
            print('\n\n\n\t\t\t#### TICKET BOOKED SUCCESSFULLY ######')
            print(f'\n{"-"*100}')
            print(F'NAME: {customer_name}\nPHONE NUMBER: {phone}')
            print(
                f'\nMOVIE NAME: {show[0][1]}\t\tMOVIE TIME: {show[0][2]}\nHALL NO:{self.__hall_no}')
            str = ''
            for i in list_of_tup:
                str += chr(i[0] + ord('A'))
                str += f'{i[1]} '
            print('TRICKETS: ', str)
            print(f'\n{"-"*100}')

        if flag:
            print(f'{"-"*100}\n>>>>>>THIS ID DOES NOT EXIST\n{"-"*100}')

    def view_show_list(self):
        print(f'\t\t{"#"*50}')
        print(f'\t\t\t\t ALL SHOW LIST')
        print()
        print(f"{'_'*100}")
        for i in self.__show_list:
            viewing = f'MOVIE ID\t\t\t\tMOVIE NAME\t\t\t\t\tMOVIE TIME\n{i[0]}\t\t\t\t\t{i[1]}\t\t\t\t\t{i[2]}'
            print(viewing)
            print(f'{"_"*100}')

    def __seat_show_ui(self, lst):
        new_lst = copy.deepcopy(lst)
        txt = []
        for i in range(65, 91):
            txt.append(chr(i))
        for i, v in enumerate(new_lst):
            for i1, j in enumerate(v):
                if new_lst[i][i1] == 'Empty':
                    new_lst[i][i1] = f'{txt[i]}{i1}'
        return new_lst

    def view_available_seats(self, id):
        flag = 0
        for key, val in self.__seats.items():
            if key == id:
                print('\n\n')
                print(f'\t\t{"#"*50}')
                print('\t\t\t\tAVAILABLE SEATS')
                show = []
                for i in self.__show_list:
                    if i[0] == id:
                        show.append(i)
                        break
                print(
                    f'\nMOVIE NAME:\t{show[0][1]}\tMOVIE TIME:\t{show[0][2]}\t')
                print('_'*100, '\n')
                for val2 in self.__seat_show_ui(val):
                    for val3 in val2:
                        print(val3, end="\t\t")
                    print()
                flag = 1
                print('_'*100)
                break
        if not flag:
            print(f'{"-"*100}\n>>>>>>THIS ID DOES NOT EXIST\n{"-"*100}')
        print('\n\n')


def convert_row_col(seat_no):
    row = None
    col = None
    for i in seat_no:
        if i.isalpha():
            row = ord(i) - ord('A')
        else:
            col = int(i)
    return tuple((row, col))


star_cinema = StarCinema()
hall = Hall(5, 3, 10)
hall.entry_show('abc123', 'Holly Faak', '10:30AM')
hall.entry_show("abc12", "JANEMON 20", '2: 00PM')
while True:
    print('1. VIEW ALL SHOWS TODAY\n2. VIEW AVAILABLE SEATS\n3. BOOK TICKET \n4. EXIT')
    option = int(input('ENTER OPTION : '))
    if option == 4:
        break
    elif option == 1:
        hall.view_show_list()
    elif option == 2:
        id = input('ENTER YOUR ID : ')
        hall.view_available_seats(id)
    elif option == 3:
        name = input('ENTER YOUR NAME : ')
        phone = input('ENTER YOUR PHONE NUMBER : ')
        id = input('ENTER SHOW ID : ')
        number_ticket = int(input('NUMBER OF TRICKETS : '))
        seats_no = []
        seat = ""
        for i in range(number_ticket):
            seat_no = input('ENTER YOUR SEATS NUMBER : ')
            seat += seat_no + ' '
            row_col = convert_row_col(seat_no)
            seats_no.append(row_col)
        hall.book_seats(name, phone, id, seats_no)
