import PySimpleGUI as sg
import matplotlib

class IllegalAbilityValues(Exception):
    pass

class IllegalQualificationValues(Exception):
    pass

class IllegalPromotions(Exception):
    pass

class general:
    def __init__(self, name: str, inf_ab: int, cav_ab: int, art_ab: int, navy_ab: int, port_ab: int
                 , trade_ab: int, move_ab: int, train_ab: int, skills: list, rank: int, noble_class: int):
        self.__name = name
        if inf_ab < 0 or inf_ab > 5:
            raise IllegalAbilityValues("Error: general's infantry ability has illegal values")
        self.__inf_ab = inf_ab
        if cav_ab < 0 or cav_ab > 5:
            raise IllegalAbilityValues("Error: general's cavalry ability has illegal values")
        self.__cav_ab = cav_ab
        if art_ab < 0 or art_ab > 5:
            raise IllegalAbilityValues("Error: general's artillery ability has illegal values")
        self.__art_ab = art_ab
        if navy_ab < 0 or navy_ab > 5:
            raise IllegalAbilityValues("Error: general's navy ability has illegal values")
        self.__navy_ab = navy_ab
        if port_ab < 0 or port_ab > 5:
            raise IllegalAbilityValues("Error: general's port ability has illegal values")
        self.__port_ab = port_ab
        if trade_ab < 0 or trade_ab > 5:
            raise IllegalAbilityValues("Error: general's trade ability has illegal values")
        self.__trade_ab = trade_ab
        if move_ab < 0 or move_ab > 5:
            raise IllegalAbilityValues("Error: general's move ability has illegal values")
        self.__move_ab = move_ab
        if train_ab < 0 or train_ab > 5:
            raise IllegalAbilityValues("Error: general's train ability has illegal values")
        self.__train_ab = train_ab

        self.__skills = []
        for i in skills:
            if (type(i) == str and len(i) > 3):
                self.__skills += [i]

        if rank < 0 or rank > 150:
            raise IllegalQualificationValues("Error: general's rank has illegal values")
        self.__rank = rank

        if noble_class < 0 or noble_class > 10:
            raise IllegalQualificationValues("Error: general's noble class has illegal values")
        self.__noble_class = noble_class

        self.__rank_exp = 0
        self.__noble_class_exp = 0

    def __str__(self):
        try:
            return self.__name + " " + str(self.__inf_ab) + " " + str(self.__cav_ab) + " " + str(self.__art_ab) \
                   + str(self.__navy_ab) + " " + str(self.__port_ab) + " " + str(self.__trade_ab) + " "\
                   + str(self.__move_ab) + " " + str(self.__train_ab) + " " + str(self.__skills) + " " + str(self.__rank) \
                   + " " + str(self.__noble_class)
        except:
            raise Exception()

    def __eq__(self, other):
        try:
            if type(other) != general:
                return False
            return self.__name == other.name and self.__inf_ab == other.__inf_ab and self.__cav_ab == other.__cav_ab \
                   and self.__art_ab == other.__art_ab and self.__navy_ab == other.__navy_ab and self.__port_ab == other.\
                       __port_ab and self.__trade_ab == other.__trade_ab
        except:
            raise Exception()

    def get_name(self):
        try:
            return self.__name
        except:
            raise Exception()

    def get_infantry_ability(self):
        try:
            return self.__inf_ab
        except:
            raise Exception()

    def get_cavalry_ability(self):
        try:
            return self.__cav_ab
        except:
            raise Exception()

    def get_artillery_ability(self):
        try:
            return self.__art_ab
        except:
            raise Exception()

    def get_navy_ability(self):
        try:
            return self.__navy_ab
        except:
            raise Exception()

    def get_port_ability(self):
        try:
            return self.__port_ab
        except:
            raise Exception()

    def get_trade_ability(self):
        try:
            return self.__trade_ab
        except:
            raise Exception()

    def get_move_ability(self):
        try:
            return self.__move_ab
        except:
            raise Exception()

    def get_train_ability(self):
        try:
            return self.__train_ab
        except:
            raise Exception()

    def set_rank(self, adjustment: int, promotion=False):
        if promotion:
            if adjustment == 1:
                self.rank += 1
            else:
                raise IllegalPromotions
        else:
            pass

    def get_rank(self):
        try:
            return self.__rank
        except:
            raise Exception()

    def get_rank_experience(self):
        try:
            return self.__rank_exp
        except:
            raise Exception()

    def set_noble_class(self):
        pass

    def get_noble_class(self):
        try:
            return self.__noble_class
        except:
            raise Exception()

    def get_noble_class_experience(self):
        try:
            return self.__noble_class_exp
        except:
            raise Exception()

    def regroup(self, other):
        pass

    def GUI(self):
        sg.theme('BluePurple')

        layout = [[sg.Text('Your general name appear here:'),
                sg.Text(size=(25, 1), key='-OUTPUT-')],
                [sg.Input(key='-IN-')],
                [sg.Button('Proceed'), sg.Button('Exit')]]

        window = sg.Window('European War 4: Napoleon - General Analysis', layout)

        while True:
            event, values = window.read()
            print(event, values)

            if event in (None, 'Exit'):
                break
            if event == 'Proceed':
                window['-OUTPUT-'].update(values['-IN-'])

        window.close()

Napoleon = general("Napoleon", 3, 3, 5, 2, 3, 3, 3, 3, ["Banner", "Infantry Tactics", "Engineering", "Siege Master"], 98, 5)
Napoleon.GUI()