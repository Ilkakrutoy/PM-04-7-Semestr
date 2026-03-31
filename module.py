class Module:
    def __init__(self, name, module_type):
        self.name = name
        self.module_type = module_type

    def validate(self):
        if not self.name:
            return False, "Имя модуля не задано"
        if not self.module_type:
            return False, "Тип модуля не задан"
        return True, "Модуль валиден"
