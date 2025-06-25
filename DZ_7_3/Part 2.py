def requires_access(func):
    def wrapper(self,*args,**kwargs):

        if args:
            employee, zone = args
        elif kwargs:
            employee, zone = kwargs.values()

        if (zone in self.get_open()) or (zone in self.get_close() and zone in employee.get_zone()):
            print('    есть допуск')
            rez = func(self,*args,**kwargs)
            return rez

        else:
            print('    НЕТ допуска')
            self.add_denied(employee,zone)

    return wrapper

def log_access(func):
    def wrapper(self,*args, **kwargs):
        print('===>Попытка входа')
        rez = func(self,*args,**kwargs)
        print('===>Попытка окончена\n')
        return rez
    return wrapper

class Employee:

    def __init__(self, name: str, access_zone = None):
        self.__name = name
        self.__access_zone = access_zone or []

    def get_name(self):
        return self.__name

    def get_zone(self):
        return self.__access_zone

class SecuritySystem:
    def __init__(self):
        self.access_granted = []
        self.access_denied = []
        self.__open_area = ['Lobby','Cafeteria']
        self.__close_area = ['Office','Storage']

    def add_denied(self, employee, zone):
        self.access_denied.append(f'{employee.get_name()} = {zone}')

    def get_open(self): return self.__open_area

    def get_close(self): return self.__close_area

    @log_access
    @requires_access
    def enter_zone(self, employee, zone):
        self.access_granted.append(f'{employee.get_name()} = {zone}')
        print('    Доступ ВЫДАН')

e = Employee('Ivan', ["Office"])
SS = SecuritySystem()
SS.enter_zone(e,'Storage')
SS.enter_zone(e,'Office')
SS.enter_zone(e,'Cafeteria')

print('\nСписок запретов', SS.access_denied,'\nСписок разрешений', SS.access_granted)